import boto3
import pandas as pd 
import os 
import numpy as np

client = boto3.client('redshift')


# check on revisions to the db
revisions = client.describe_cluster_db_revisions(ClusterIdentifier="cluster_name")
print(revisions)

# check the parameters of the db 
params = client.describe_cluster_parameters(ParameterGroupName="parameter_group_name")
print(params)

# describe the cluster 
clust = client.describe_clusters(ClusterIdentifier = "cluster_name") # no args actually required for this so if I don't put a clustername I will get for all clusters 
print(clust)

# modify my cluster - ie change type, node, number of nodes, snapshot retention period, maintenance window etc. 
client.modify_cluster(ClusterIdentifier="cluster_name", NodeType="ds2.xlarge") # ...

 
# rotate encryption key 
keyz = client.rotate_encryption_key(ClusterIdentifier = "cluster_name")