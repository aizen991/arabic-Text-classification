import tensorflow as tf
import numpy as np
import os


model = tf.keras.models.load_model("model")

prediction_np = model.predict(["يمكن أن يساعدك التخطيط المالي الجيد على الادخار والاستثمار بشكل أفضل وتحقيق مكاسب سريعة، ويتطلب ذلك تحديد أهدافك والمبالغ التي يمكن أن تنفقها وتقييم المخاطر واختيار الوقت المناسب للاستثمار."])
print(prediction_np)

prediction = np.argmax(prediction_np[0],axis=0)
print(prediction)

class_names =  os.listdir("dataset")

class_names.sort()

print(class_names[prediction],":",prediction_np[0][prediction])
