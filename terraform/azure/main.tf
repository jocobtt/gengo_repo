
######################################
# configure azure provider
######################################

provider "azurerm" {
  version = "~2.0"
  features {}

  subscription_id = "my_id"
  client_id       = "client_id"
  client_secret   = "client_sec"
  tenant_id       = "tenant_id"
}

#####################################
# create resource group 
#####################################
resouce "azurerm_resource_group" "tf_group" {
  name      = "tf_resource"
  location  = "eastus"

  tags = {
    environment = "Terraform Demo"
    ResourceOnwer = "jacob.braswell@sas.com
  }
}

###################################
# Create virtual network 
##################################
resource "azurerm_virtual_network" "tf_network" {
  name                 = "jacob-tf"
  address_space        = ["10.0.0.0/16"]
  location             = "eastus"
  resource_group_name  = azure_resource_group.tf_group.name

  tags = {
    environment = "Terraform Demo"
  }
}

#############################
# Create subnet 
#############################
# https://docs.microsoft.com/en-us/azure/terraform/terraform-create-complete-vm

