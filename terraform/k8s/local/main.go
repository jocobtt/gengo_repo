provider "kubernetes" {}

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
