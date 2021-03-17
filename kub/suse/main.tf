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
  count                  = 5
  name                   = "suse_nic"
  location               = "eastus"
  resource_group_name    = azurerm_resource_group.myterraformgroup.name

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
  count                 = 5
  name                  = "suse_vm"
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

 
