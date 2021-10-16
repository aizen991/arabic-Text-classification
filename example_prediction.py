import tensorflow as tf
import numpy as np
import os


model = tf.keras.models.load_model("model")

prediction_np = model.predict(["يساعد الجوز المليء بمضادات الأكسدة وفيتامين ب على حماية بشرتك من العوامل البيئية الضارة مثل التعرض للشمس والأوساخ والتلوث والشوائب الأخرى، وهذا بدوره يمنع تلف الجلد وظهور الخطوط الدقيقة والتجاعيد المبكرة، بالإضافة إلى ذلك، فإن وجود فيتامين E يرطب بشرتك بشكل مكثف ويعزز إنتاج الكولاجين للحفاظ على بشرتك أكثر شبابًا."])
print(prediction_np)

prediction = np.argmax(prediction_np[0],axis=0)
print(prediction)

class_names =  os.listdir("dataset")

class_names.sort()

print(class_names[prediction],":",prediction_np[0][prediction])
