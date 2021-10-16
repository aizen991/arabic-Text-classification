import tensorflow as tf
import numpy as np
import os


model = tf.keras.models.load_model("model")

prediction_np = model.predict(["لطالما أخذت تسريحة الشعر المبلل شعبية واسعة كونها تسريحة سهلة وتليق بالجميع بمختلف أنواع الشعر، واليوم هي سيدة الموضة العالمية بعد سيطرتها على عروض الجمال لربيع 2022. تعرفي على كيفية الحصول على هذه التسريحة بالخطوات"])
print(prediction_np)

prediction = np.argmax(prediction_np[0],axis=0)
print(prediction)

class_names =  os.listdir("dataset")

class_names.sort()
print(class_names)
print(class_names[prediction],":",prediction_np[0][prediction])
