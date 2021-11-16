from kubernetes import client, config

# for this file you will need to install the kubernetes python project - https://github.com/kubernetes-client/python

def main(namespace):

    config.load_kube_config("~/.kube/jared-cluster.conf")

    v1 = client.CoreV1Api()
    print("List all of the pods we have in our namespace")

    pods = v1.list_namespaced_pod(namespace = namespace, watch=False)
    for item in pods.items:
        main_item = item.metadata.name
    return main_item

if __name__ == '__main__':
    main(namespace="production-pit-lts-20201")
