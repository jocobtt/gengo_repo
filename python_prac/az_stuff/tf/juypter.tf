resource "kubernetes_manifest" "namespace_jupyterlab" {
  manifest = {
    "apiVersion" = "v1"
    "kind" = "Namespace"
    "metadata" = {
      "name" = "jupyterlab"
    }
  }
}

resource "kubernetes_manifest" "deployment_jupyter" {
  manifest = {
    "apiVersion" = "apps/v1"
    "kind" = "Deployment"
    "metadata" = {
      "labels" = {
        "app" = "jupyter"
      }
      "name" = "jupyter"
      "namespace" = "jupyterlab"
    }
    "spec" = {
      "replicas" = 1
      "selector" = {
        "matchLabels" = {
          "app" = "jupyter"
        }
      }
      "template" = {
        "metadata" = {
          "labels" = {
            "app" = "jupyter"
          }
        }
        "spec" = {
          "containers" = [
            {
              "image" = "registry.unx.sas.com/jabras/gpu-sas:latest"
              "imagePullPolicy" = "Always"
              "name" = "jupyter"
              "ports" = [
                {
                  "containerPort" = 8080
                  "name" = "http"
                  "protocol" = "TCP"
                },
              ]
            },
          ]
        }
      }
    }
  }
}

resource "kubernetes_manifest" "service_jupyter" {
  manifest = {
    "apiVersion" = "v1"
    "kind" = "Service"
    "metadata" = {
      "labels" = {
        "app" = "jupyter"
      }
      "name" = "jupyter"
      "namespace" = "jupyterlab"
    }
    "spec" = {
      "ports" = [
        {
          "name" = "http"
          "port" = 80
          "protocol" = "TCP"
          "targetPort" = "http"
        },
      ]
      "selector" = {
        "app" = "jupyter"
      }
      "type" = "ClusterIP"
    }
  }
}

