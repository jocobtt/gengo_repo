
# cognitive services endpoint 
output "computer_vision_endpoint" {
  value = "${var.endpoint}"
}

output "primary_access_key" {
  value = 
}

# automate outputs
output "automation_schedule_start_time" {
  value = "${azurerm_automation_schedule.one-time.start-time}"
}

output "automation_scheduel_week_interval" {
  value = "${azurerm_automation_schedule.hour.interval}"
}


# azureml endpoint 
output "azureml_endpoint" {
  value = blah
}

# aks outputs 
output "client_certificate" {
  
}

output "id" {
  value = azurerm_kubernetes_cluster.example.id
}

output "kube_config" {
  value = azurerm_kubernetes_cluster.example.kube_config_raw
}

output "client_key" {
  value = azurerm_kubernetes_cluster.example.kube_config.0.client_key
}

output "client_certificate" {
  value = azurerm_kubernetes_cluster.example.kube_config.0.client_certificate
}

output "cluster_ca_certificate" {
  value = azurerm_kubernetes_cluster.example.kube_config.0.cluster_ca_certificate
}

output "host" {
  value = azurerm_kubernetes_cluster.example.kube_config.0.host
}

