# Kubernetes v1.18 on Suse Linux Distribution pt. 2:

* Note: this is a continuation of my last blog where I walked through how to provision a cluster on a SUSE Linux Distribution. If you haven't seen that blog first check it out here - <link to first blog>

Now that we have seen how to install a full on Kubernetes cluster to deploy Viya 4 instance. In order to do this we will follow the same steps that we showed earlier to create a multi node Kubernetes cluster. 


# Creating multiple VMs using Terraform 

Terraform is an infrastructure automation tool that allows you to provision complex infrastructure in simple and repeatable ways. 

```bash 

provider "azurerm" {
  version = "~>2.0"
  features {}
}

resource "azurerm_resource_group" "suse_rg" {
  name     = "suse_rg"
  location = "eastus"
  tags = {
    environment   = "test"
    resourceowner = "jacob.braswell@sas.com"
  }
}

# create virtual network 
resource "azurerm_virtual_network" "mytfnetwork" {
  name                = "suse_net"
  address_space       = ["10.0.0.0/16"]
  location            = "eastus"
  resource_group_name = azurerm_resource_group_myterraformgroup.name 
  tags = {
    environment = "test" 
  }
}

# subnet creation 
resource "azurerm_subnet" "tf_subnet" {
  name                 = "subnet_suse"
  resource_group_name  = azurerm_resource_group.myterraformgroup.name
  virtual_network_name = azurerm_virtual_network.myterraformnetwork.name
  address_prefixes     = ["10.0.2.0/24"]
}

# create public IP 
resource "azurerm_public_ip" "my_tf_ip" {
  name                          = "suse_publicip"
  location                      = "eastus"
  resource_group_name           = azurerm_resource_group.myterraformgroup.name
  allocation_method             = "Dynamic"
  tags = {
    environment = "test" 
  }
}

# create network security group 
resource "azurerm_network_security_group" "tf_security" {
  name                = "suse_securityg"
  location            = "eastus"
  resource_group_name = azurerm_resource_group.myterraformgroup.name
  security_rule {
    name                       = "SSH"
    priority                   = 1001
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

# create network interface 
resource "azurerm_network_interface" "tf_nic" {
  count               = 5
  name                = "suse_nic"
  location            = "eastus"
  resource_group_name = azurerm_resource_group.myterraformgroup.name
  ip_configuration {
    name                          = "suse_NicConfig"
    subnet_id                     = azurerm_subnet.myterraformsubnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.myterraformpublicip.id
  }
}

# connect the security group to the network interface 
resource "azurerm_network_interface_security_group_association" "tf_sec" {
  network_interface_id      = azurerm_network_interface.myterraformnic.id
  network_security_group_id = azurerm_network_security_group.myterraformnsg.id
}

# create vm 
resource "azurerm_linux_virtual_machine" "suse_vm" {
  name                  = "suse_vm"
  count                 = 5
  location              = "eastus"
  resource_group_name   = azurerm_resource_group.myterraformgroup.name
  network_interface_ids = [azurerm_network_interface.myterraformnic.id]
  size                  = "Standard_DS1_v2"
  os_disk {
    name                 = "suse_os"
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
  }
  source_image_reference {
    publisher = "SUSE"
    offer     = "SLES"
    sku       = "15"
    version   = "lastest"
  }
  computer_name                   = "suse_vm"
  admin_username                  = "azureuser"
  disable_password_authentication = true
  admin_ssh_key {
    username   = "azureuser"
    public_key = tls_private_key.example_ssh.public_key_openssh
  }
  tags = {
    resourceowner = "jacob.braswell00@gmail.com"
  }
}

```
Above is the script we will use to create 5 Suse Linux virtual machines to set up our cluster on. We can run the above script by setting up a service principle for our Azure account and then execute like we would any other terraform script by running the below code:
```
terraform init
terraform apply 
```

For more explanation about what the terraform script is doing besides what is in the comments in the script refer to [this article](https://docs.microsoft.com/en-us/azure/developer/terraform/create-linux-virtual-machine-with-infrastructure).  

## Tie the Kubernetes Cluster Nodes Together 
Now that we have our virtual machines provisioned we can now install our dependencies on each of our virtual machines in order to set up our cluster. We will follow the steps listed in my other blog to set up kubeadm, kubelet, our container runtime crio, docker and other dependecies. We are going to use kubeadm to connect our other virtual machines that we have provisioned to our main virtual machine in a worker node with a master node set up. In order to set up our main virtual machine as the master node we are going to follow the instructions in our blog by running `kubeadm init` to initialize the creation of the Kubernetes control plane. When we have run this step we will receive a token in the output of that command that will allow us to be able to connect the rest of our virtual machines as worker nodes to our cluster. 

![kubeadm_join](/img/kubeadm_join.png)

In order to join each of our worker nodes we will need to ssh into each of our machines and run the above `kubeadm join` command with our provided token, as listed above, after we have installed kubeadm and it's dependencies. From there we can go back into our main control-plane node's virtual machine to install Viya on our cluster. 

## Install Viya on it
Now that we have our Kubernetes cluster provisioned as desired we can now attempt to install Viya 4 in our cluster. Note that we are running the below steps from our control plane cluster.  

Since we already have Kubernetes version 1.18 installed as well as Kustomize version 3.7 installed we have our preinstall requirements met. Now what we need to do is set up our ingress, set up our database, set up our storage class for our inner cluster purposes, set up a DNS name, and set up our ldap as needed.  

#### Ingress - This will need to be adjusted... Not cloud generic cuz ip won't create 
There are various ways to accomplish setting up an ingress for our purposes, we can set up a simple nodeport for us to access to or provision a kubernetes loadbalancer. We We can simply pull down Nginx's static deployment manifests and incorporate those manifests and a manifest that whitelists our desired ip's into a `kustomization.yaml` file like so below:

```yaml
---
apiVersion: kustomize.config.k8s.io/v1beta1
namespace: ingress-nginx 
resources:
- static.yaml 

transformers:
- load-balancer-source-range.yaml 
```

Here is an example of what our `load-balancer-source-range.yaml` file would look like: 

```yaml 
---
apiVersion: builtin
kind: PatchTransformer
metadata:
  name: load-balancer-source-range
patch: |-
  - op: add
    path: /spec/loadBalancerSourceRanges
    value: 
    - 149.173.0.0/16
    - 10.244.0.0/16
target:
  app: ingress-nginx
  kind: Service
  name: ingress-nginx
  version: v1
```

To check to see whether our load balancer service has properly been provisioned we can run `kubectl get svc -n ingress-nginx` 


#### Database 
For setting up our database we have a few different options that we can consider and our decision depends on both preference and performance considerations. We have the option to either use an in cluster crunchy sql database or we can provision a azure postrgresql database instance to act as our storage database for our cluster. For this example we will use the in cluster database option. To do this we simple need to include the specifications in our Viya deployment's `kustomization.yaml` file and then our crunchy data pods will deploy with our Viya deployment. The specifc addon to our `kustomization.yaml` file for our Viya deployment will look like so: 

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: viya4-ns

resources:
...
- sas-bases/overlays/crunchydata
- sas-bases/overlays/internal-postgres
...
```

#### Storage Class 
For the storage class for our cluster we will utilize [this](https://charts.helm.sh/stable) helm chart that will provision what we need. In order to use this resource we can provision it like so:

```bash
helm repo add stable https://charts.helm.sh/stable # add the stable helm repo so we can install the nfs-client chart 
kubectl create ns nfs-server  # create the namespace for our storage class 
# install the helm chart for our nfs server. Set the server ip address and path where it is located so it can be used by a persistent volume claim in our Viya deployment. 
helm install nfs stable/nfs-client-provisioner --set nfs.server=${NFSIP} --set nfs.path=/volumes --set storageClass.name="rwxclass" --namespace nfs-server

```

#### LDAP 
To set up our LDAP we can use GEL's openldap, which is a test ldap deployment. We will create a kustomization.yaml file to use this resource, which would look like below:

```yaml
---
apiVersion: kustomize.config.k8s.io/v1beta1
namespace: ingress-nginx 
resources:
- gelldap-location in gitlab
```

#### Apply Viya manifest
We now need to install Viya on our cluster. We do this by changing into the deployment directory that we have that contains our Viya manifest. Once in that directory we will need to create a namespace for our deployment. We do this by running `kubectl create ns sus-viya`. Once we have our namespace created we can then apply our `kustomization.yaml` manifest for our deployment. But first we should explain what is going on in said manifest. 

## Access it
We can check to see if our installation has fully ran by running `kubectl get pods -n <VIYA-NAMESPACE>` which should show us that our pods are running and healthy like shown below. 

<image of working deployment> 

# Conclusion 
