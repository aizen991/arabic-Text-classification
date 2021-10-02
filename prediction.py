import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model("modele")

prediction_np = model.predict(["فنسأل الله -تعالى- أن يوفقك، وأن يزيدك حرصا على الخير، وسواء كانت الورقة المشار إليها خاصة بالموظف المذكور، أو من أوراق الكلية فلا حرج في ذلك، فالأصل أن الشخص الذي قام بتصوير تلك الورقة لن يفعل إلا ما هو مأذون له فيه تصريحا أو عرفا، وهو مؤتمن على ما في الكلية. وقد نص الفقهاء على أن المؤتمن بمقتضى الوكالة أو الحراسة، له أن يتصرف في مال من ائتمنه بقدر ما جرت العادة به من الشيء ‌اليسير ‌الذي ‌لا ‌يتشاح ‌في ‌مثله، واستدلوا لذلك بقوله تعالى: أَوْ مَا مَلَكْتُمْ مَفَاتِحَهُ أَوْ صَدِيقِكُمْ  كما قرر ذلك ابن رشد في البيان والتحصيل"])
prediction = np.argmax(prediction_np[0],axis=0)

print(prediction_np)

if prediction==0:
  print("culture  :",prediction_np[0][prediction])
elif prediction==1:
  print("finance :",prediction_np[0][prediction])
elif prediction==2:
  print("medical :",prediction_np[0][prediction])
elif prediction==3:
  print("politic :",prediction_np[0][prediction])
elif prediction==4:
  print("religion :",prediction_np[0][prediction])  
elif prediction==5:
  print("sport :",prediction_np[0][prediction])
else:
  print("tech :",prediction_np[0][prediction])