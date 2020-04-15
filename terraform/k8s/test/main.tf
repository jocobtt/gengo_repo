provider "kubernetes" {
  host                     = "https://localhost:6565"
  config_context_auth_info = "docker-for-desktop"
  config_context_cluster   = "docker-for-desktop-cluster" 
  # the above is if i want to set up config_context_cluster and auth info - not neccessary
}

# create a namespace for our cluster we are going to build 
resource "kubernetes_namespace" "tf-test" {
  metadata {
    annotations = {
      name = "tf-namespace"
    }
    
    labels = {
      mylabel = "labelz"
    }
   
    name = "terraform-ex-ns"
  }
}


# if we want to create a secret in kubernetes 
# data "kubernetes_secret" "example" {
#   metadata {
#     name = "basic-auth" # my secrets metadata
#   }
# } 
  

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
    name      = "argo-example"
    namespace = "tf-namespace"
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
