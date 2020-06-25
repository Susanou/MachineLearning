#!/usr/bin/python3

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist

(train_img, train_labels), (img_test, labels_test) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


# show and check that data was loaded
plt.figure()
plt.imshow(train_img[0])
plt.colorbar()
plt.grid(False)
# plt.show()      #deactivated for the moment

# Make data range from [0:1] instead of [0:255]
train_img = train_img / 255.0
img_test = img_test / 255.0

# Building model

model = keras.Sequential(
    [
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(50),
        keras.layers.Dense(10)
    ]
)
model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(
                  from_logits=True),
              metrics=['accuracy'])

# Training model
model.fit(train_img, train_labels, epochs=10)
test_loss, test_acc = model.evaluate(img_test, labels_test, verbose=2)

print("Test loss ", test_loss)
print("Test accuracy ", test_acc)

# Make predictions now
probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])

predictions = probability_model.predict(img_test)


def plot_image(i: int, predictions_array: list, true_label: list, img: list):
    """Function that plots all the images in the predictions and their 
    associated probability listing on a graph on the side

    Parameters
    ----------
    i : int
        index of the label and image checked
    predictions_array : list
        list of all the images that we are trying to predict the type of
    true_label : list
        label of the image
    img : list
        actual image
    """
    predictions_array, true_label, img = predictions_array, true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                         100*np.max(predictions_array),
                                         class_names[true_label]),
               color=color)


def plot_value_array(i: int, predictions_array: list, true_label: list):
    """Function thats plots the different values of prediction

    Parameters
    ----------
    i : int
        Index of the current values
    predictions_array : list
        Array containing the predictions of the current index (percentages)
    true_label : list
        True label of the current index
    """
    predictions_array, true_label = predictions_array, true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


plt.figure(figsize=(12, 10))
for i in range(15):
    plt.subplot(5, 6, 2*i+1)
    plot_image(i, predictions[i], labels_test, img_test)
    plt.subplot(5, 6, 2*i+2)
    plot_value_array(i, predictions[i], labels_test)
plt.tight_layout()
plt.show()
