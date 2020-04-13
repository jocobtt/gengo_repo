provider "kubernetes" {
  host                     = "https://localhost:6565"
  config_context_auth_info = "docker-for-desktop"
  config_context_cluster   = "docker-for-desktop-cluster" 
}

# set up pod image 
resource "kubernetes_pod" "argo" {
  metadata {
    name = "argo-example"
    labels = {
      App = "argo"
    }
  }
  
  spec {
    container {
      image = "argoproj/argocli:v2.7.2"  # check if this is right or not 
      name = "argo_test" ### once I get this figured out I will start trying to build more complex stuff 

      port {
        container_port = 80 
      }
    }
  }
}
# create service for the pod 
resource "kubernetes_service" "nginx" {
  metadata {
    name = "argo-example"
  }
  spec {
    selector = {
      App = kubernetes_pod.argo.metadata[0].labels.App
    }
    port {
      port        = 80
      target_port = 80
    }

    type = "NodePort"
  }
}

# build another resource ie another pod  
resource "kubernetes_pod" "my_other_pod"
  metadata {
    name = "nginx-add" 
    labels = { 
      app = "examp2"
    }
  }

  spec {
    container {
      image = "nginx:1.7.9"
      name  = "example"
      
      port {
        container_port = 8080
      }
    }
  }
}
