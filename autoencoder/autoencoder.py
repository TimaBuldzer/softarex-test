import keras.layers
from keras import Model, Input

from types import Dimensions


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
