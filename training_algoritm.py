import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
import os
from tensorflow.keras import losses
from tensorflow.keras import layers
import matplotlib.pyplot as plt




tf.keras.backend.clear_session()

seed=42
data_paths = 'dataset'
labels=os.listdir(data_paths) 

print(labels)
raw_data_train = tf.keras.preprocessing.text_dataset_from_directory(
    data_paths,
    labels="inferred",
    label_mode="int",
    #class_names=classes,
    #batch_size=1,
    max_length=None,
    shuffle=True,
    seed=seed,
    validation_split=None,
    subset=None,
    follow_links=False,
)





raw_data_test = tf.keras.preprocessing.text_dataset_from_directory(
    data_paths, 
    validation_split=0.2, 
    subset='validation', 
    seed=seed)





x_train=[]
y_train=[]
for text_batch, label_batch in raw_data_train:
    for i in range(len(text_batch)):
        s=text_batch.numpy()[i].decode("utf-8") 
        x_train.append(s)
        y_train.append(raw_data_train.class_names[label_batch.numpy()[i]])
        #print(label_batch.numpy()[i])
print(len(x_train))
print(len(y_train))





x_test=[]
y_test=[]
for text_batch, label_batch in raw_data_test:
    for i in range(len(text_batch)):
        s=text_batch.numpy()[i].decode("utf-8") 
        x_test.append(s)
        y_test.append(raw_data_test.class_names[label_batch.numpy()[i]])
        #print(label_batch.numpy()[i])
print(len(x_test))
print(len(y_test))






max_features = 20000
sequence_length = 500
embedding_dim = 128

vectorize_layer = TextVectorization(
    standardize="lower_and_strip_punctuation",
    max_tokens=max_features,
    output_mode="int",
    output_sequence_length=sequence_length,
)

train_text = raw_data_train.map(lambda x, y: x)
vectorize_layer.adapt(train_text)






model = tf.keras.Sequential([
    vectorize_layer,
    layers.Embedding(max_features + 1, embedding_dim),
    layers.Dropout(0.2),
    layers.GlobalAveragePooling1D(),
    layers.Dropout(0.2),
    layers.Dense(128,activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(8,activation="sigmoid"),
    ])

opt = tf.keras.optimizers.Adam(learning_rate=0.00025)
model.compile(
    loss = losses.sparse_categorical_crossentropy, optimizer=opt, metrics=['accuracy']
)

model.summary()




epochs = 6
history = model.fit(raw_data_train,validation_data=raw_data_test,epochs=epochs)

model.save("./model")






def plot_graphs(history, string):
  plt.plot(history.history[string])
  plt.plot(history.history['val_'+string])
  plt.xlabel("Epochs")
  plt.ylabel(string)
  plt.legend([string, 'val_'+string])
  plt.show()
  
plot_graphs(history, "accuracy")
plot_graphs(history, "loss")
