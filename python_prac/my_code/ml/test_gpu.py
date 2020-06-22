import tensorflow as tf 

# print out if tensorflow has a cuda gpu available 
print(tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None)


# list number of gpu's available 
#from __future__ import absolute_import, division, print_function, unicode_literals
#print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))


# list available devices to run on 
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

