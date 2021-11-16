variable "resource_group" {
    default = "azureml-tf"
}

variable "workspace_display_name" {
    default = "aml-tf-ns"
}

variable "location" {
    default = "East US"
}

variable "deploy_aks" {
    default = false
}

variable "jumphost_ussername" {
    default = "azureuser"
}

variable "jumpuser_password" {
    default = "password"
}

variable "prefix" {
    type    = string 
    default = "aml" 
}

resource "random_string" "postfix" {
    length  = 6
    special = false 
    upper   = false 
}

variable "cog_name" {
    type    = string
    default = "test_cog"
}

variable "cog_kind" {
    type    = string 
    default = "ComputerVision" 
}

variable "cog_sku_name" {
  description = "Name for our cognitive services sku"
  type        = string
  default     = "S1"
}

variable "cog_tier_name" {
  description = "Name of our cognitive service tier"
  type        = string
  default     = "Standard"
}




