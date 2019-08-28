import json
import os
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import img_to_array, array_to_img, load_img

if __name__ == "__main__":
    filepath = "/home/brian/Pictures/GSV_scrape/"
    labels_filepath = os.path.join(filepath, "labels.json")

    with open(labels_filepath, 'r') as f:
        data = json.load(f)

    image_names = sorted(list(data.keys()))

    labeled_image_names = image_names[:1350]
    for start, stop in zip(list(range(0, 950, 50)), list(range(50, 1000, 50))):
        for image in labeled_image_names[start: stop]:
            img = img_to_array(load_img(os.path.join(filepath, image)))
            img = img.reshape((1,) + img.shape)
            try:
                images = np.vstack((images, img))
                labels.append(data[image])
            except NameError:
                images = img
                labels = [data[image]]
        print("DONE WITH THIS 1")
        labels = np.array(labels)


        model = Sequential()
        model.add(Conv2D(32, (3, 3), input_shape=(3, 640, 2560)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))

        model.compile(loss='binary_crossentropy',
                      optimizer='rmsprop',
                      metrics=['accuracy'])
        print("DONE WITH THIS 1")

        model.fit(images, labels, batch_size=25, epochs=10)
        print("DONE WITH THIS 1")
    guess = model.evaluate(test_images, test_labels, batch_size=500)
    print(guess)
