import tensorflow as tf
print("TensorFlow version:", tf.__version__) # print tf version
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU'))) # print how many gpus are available

