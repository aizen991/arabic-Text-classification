import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model("modele")

prediction_np = model.predict(["وبلغ الخوف من تيك توك حد أن إنستغرام نصح صُنّاع المحتوى بأنهم إذا أعادوا تدوير مقاطع الفيديو التي تحتوي على علامة تيك توك المائية كمشاركات ضمن ميزة ريلز في إنستغرام فإن محتواهم سيكون أقل قابلية للاكتشافوتقول تيك توك إن أكبر أسواقها موجودة في الولايات المتحدة وأوروبا والبرازيل وجنوب شرقي آسيا مع أن مقر الشركة الأم  (ByteDance) يقع في الصين بالطبع، واجهت تيك توك تهديدات تنظيمية شديدة في السنوات الأخيرة، فعلى سبيل المثال حاول الرئيس الأميركي السابق دونالد ترامب منع المعاملات التجارية الأميركية مع تيك توك، وفي الهند التي تضم 1.36 مليار نسمة تم حظر تيك توك منذ العام الماضي.وعلى الرغم من كل ذلك، فإن تطبيق تيك توك يواصل إظهار نمو مثير للإعجاب؛ ففي الشهر الماضي فقط اشترت بايت دانس -الشركة الأم لتيك توك- شركة تصنيع أجهزة الواقع الافتراضي بيكو (Pico)، وذلك يشير إلى توسع مستقبلي محتمل للشركة في عالم الواقع الافتراضي."])
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
