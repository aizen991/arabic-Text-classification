import tensorflow as tf
import numpy as np
import os
import sys


model = tf.keras.models.load_model("model")


prediction_np = model.predict([sys.argv[1]])
print(prediction_np)

prediction = np.argmax(prediction_np[0],axis=0)
print(prediction)

class_names =  os.listdir("dataset")

class_names.sort()
print(class_names[prediction],":",prediction_np[0][prediction])
