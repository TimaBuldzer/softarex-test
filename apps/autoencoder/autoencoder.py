from io import BytesIO

import keras.layers
from keras import Model, Input
import cv2
import numpy as np
from keras_preprocessing.image import array_to_img
from apps.autoencoder.types import Dimensions, np_array


class Autoencoder:
    @staticmethod
    def build(dimensions: Dimensions, depth: int = 1) -> Model:
        inputs = Input(shape=(dimensions.height, dimensions.width, depth))
        x = inputs

        x = keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same', name='Conv1')(x)
        x = keras.layers.MaxPooling2D((2, 2), padding='same', name='pool1')(x)
        x = keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same', name='Conv2')(x)
        x = keras.layers.MaxPooling2D((2, 2), padding='same', name='pool2')(x)

        x = keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same', name='Conv6')(x)
        x = keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same', name='Conv7')(x)

        x = keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same', name='Conv3')(x)
        x = keras.layers.UpSampling2D((2, 2), name='upsample1')(x)
        x = keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same', name='Conv4')(x)
        x = keras.layers.UpSampling2D((2, 2), name='upsample2')(x)
        x = keras.layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same', name='Conv5')(x)

        autoencoder = Model(inputs, x, name="autoencoder")
        autoencoder.compile(loss="binary_crossentropy", optimizer='adam')
        return autoencoder

    def __prepare(self, pth: str) -> np_array:
        data = []
        dimensions = Dimensions(420, 540)
        image = cv2.imread('media/' + pth)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (dimensions.width, dimensions.height))
        data.append(image)
        data = np.expand_dims(data, axis=-1)
        data = np.array(data, dtype="float32") / 255.0
        return data

    def predict(self, image_path: str) -> BytesIO:
        autoencoder = keras.models.load_model('apps/autoencoder/autoencoder_model')
        prediction = autoencoder.predict([self.__prepare(image_path)])
        img = array_to_img((prediction[0] * 255).astype("uint8"))
        temp = BytesIO()
        img.save(temp, format="png")
        return temp
