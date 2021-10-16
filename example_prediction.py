import tensorflow as tf
import numpy as np
import os


model = tf.keras.models.load_model("model")

prediction_np = model.predict(["اختارت النجمة درة زروق في اليوم الثاني من مهرجان الجونة السينمائي الدولي إطلالة جذابة تشبه الأميرات وصُمم الفستان من توقيع المصمّمة المصرية ياسمين يايا، فتألقت بفستان مزين بالورود النافرة من قماش الشيفون والدانتيل المُطرز اللامع باللون الأوف وايت والبرونزي وجاء بتصميم الكشكش المنسدل على التنورة المنفوشة المصممة من الشيفون البنفسجي الفاتح، وارتدت درة مع هذا الفستان صندل بكعب رفيع باللون الفضي اللامع مع المجوهرات الفاخرة المصنوعة من الذهب الأبيض والألماس حيث ارتدت أقراط متدلية وأساور رفيعة."])
print(prediction_np)

prediction = np.argmax(prediction_np[0],axis=0)
print(prediction)

class_names =  os.listdir("dataset")

class_names.sort()
print(class_names)
print(class_names[prediction],":",prediction_np[0][prediction])
