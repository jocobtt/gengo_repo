from kubernetes import client, config
import os 
import pandas as pd 

# https://stackoverflow.com/questions/57365755/python-kubernetes-watch-pod-logs-not-working
# https://stackoverflow.com/questions/56124320/how-to-get-log-and-describe-of-pods-in-kubernetes-by-python-client/56128463

def get_logs(namespace, kube_config, ingress_ns, df_name, log_size):
    config.load_kube_config(kube_config)
    v1 = client.CoreV1Api()

    pod_name = []
    logs = []
    dns_ip_address = []
    container_name = []
    time_created = []
    log_timestamp = [] # this is on the first part of the log output - don't need? 
    pod_status = [] # either running, completed 

    
    print("starting loop through pods...")
    # get pod logs 
    pods = v1.list_namespaced_pod(namespace = namespace, watch=False)
    for item in pods.items:
        pod_name = item.metadata.name
        container_name = item.spec.containers[0].name
        pod_desc = v1.read_namespaced_pod(name = item.metadata.name, namespace = namespace)
        ip = v1.list_namespaced_service(namespace = ingress_ns)
        dns_ip_address = ip.items[0].status.load_balancer.ingress[0].ip
        pod_status = pod_desc.phase
        time_created = pod_desc.status.start_time


        # log logic - still need to fix this part?
        try:
            if"Running" in pod_desc.status.phase:
                logs = v1.read_namespaced_pod_log(name = item.metadata.name, container = container_name, namespace = namespace, timestamps = True, pretty = True, tail_lines = log_size)
            else: 
                logs = "NA"  
        except ApiException as ex:
            logs = ex


    df = pd.DataFrame({'pod_name': pod_name, 'cont_logs': logs, 'dns_ip_address': dns_ip_address, 'cont_logs': logs, 'container_name': container_name, 'time_created': time_created, 'pod_status': pod_status})
    df.to_csv(df_name)
    
    print("loop completed")
    # get error messages from our pods in a different script 
    # save our pod_logs 

if __name__ == '__main__':
    get_logs(namespace="viya", kube_config= "~/.kube/gtp-config.conf", ingress_ns = 'ingress-nginx', df_name = 'pod_logs.csv')







