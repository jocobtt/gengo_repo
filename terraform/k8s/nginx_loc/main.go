# configure k8s provider and connect to our kubernetes API server
provider "kubernetes" {
  host                     = "https://localhost:6443"
  config_context_auth_info = "docker-for-desktop"
  config_context_cluster   = "docker-for-desktop-cluster"
}



# this is where we call out what pod we are going to pull
resource "kubernetes_pod" "nginx_server" {
  metadata {
    name = "nginx-test"
    labels {
      App = "nginx-server"
    }
  }
  spec {
    container {
      image = "nginx:1.7.8"
      name = "example"
      
      port {
        container_port = 80
      }
    }
  }
}

# where we set up the service
resource "kubernetes_service" "nginx_server" {
  metatdata {
    name = "nginx-test"
  }
  spec {
    selector {
      App = "${kubernetes_pod.nginx_server.metadata.0.labels.App}"
    }
    port {
      port = 80
      target_port = 80 
    }
    
    type = "LoadBalancer"
  }
}

output "lb_hostname" {
  value = "${kubernetes_service.nginx_server.load_balancer_ingress.0.hostname}"
}

# then run terraform plan and apply 
