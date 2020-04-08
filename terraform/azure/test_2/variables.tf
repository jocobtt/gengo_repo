variable "client_id" {}
variable "client_secret" {}

variable "agent_count" {
    default = 3
}

variable "ssh_public_key" {
    default = "~/.ssh/id_rsa.pub"
}

variable "dns_prefix" {
    default = "futureai"
}

variable cluster_name {
    default = "futureai"
}

variable resource_group_name {
    default = "gophers-aks-eastus2"
}

variable location {
    default = "East US 2"
}

