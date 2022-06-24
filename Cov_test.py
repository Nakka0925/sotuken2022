import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
#from keras import layers, models
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
from datasets import data_gain
import matplotlib.pyplot as plt
from tensorflow.keras.utils import plot_model


file_list, label_list = data_gain()
#print(label_list)
file_list = [file.astype(float)/255.0 for file in file_list]

#file_list = np.array(file_list)

train_x, valid_x, train_y, valid_y = train_test_split(file_list, label_list, test_size=0.2)


train_y = np.array(train_y)
valid_y = np.array(valid_y)

train_x = np.array(train_x)
valid_x = np.array(valid_x)


x_val = valid_x[:755]
y_val = valid_y[:755]

test_x = valid_x[755:]
test_y = valid_y[755:]


model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(192, 192, 3)))
model.add(layers.Dropout(0.3))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.Dropout(0.3))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Dropout(0.3))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Dropout(0.3))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())


model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(4, activation='softmax'))

plot_model(model, show_shapes=True, to_file='model.png')

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_x,
                    train_y, 
                    epochs=10,
                    batch_size=32,
                    validation_data=(x_val, y_val),
                    verbose=1)

model.save('saved_model/my_model')

test_loss, test_acc = model.evaluate(test_x,  test_y, verbose=2)

print('\nTest accuracy:', test_acc)
print('\nTest loss:', test_loss)
predictions = model.predict(test_x)

print(predictions[0])

history_dict = history.history
#print (history_dict.keys())

import matplotlib.pyplot as plt

acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)


plt.plot(epochs, loss, marker="o", label='Training loss')

plt.plot(epochs, val_loss, marker="o", label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig("loss.png")
#plt.show()

plt.clf()  # 図のクリア

plt.plot(epochs, acc, marker="o", label='Training acc')
plt.plot(epochs, val_acc, marker="o", label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig("accuracy.png")
#plt.show()
