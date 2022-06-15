import keras.layers
from keras import Model, Input


class Autoencoder:
    @staticmethod
    def build(width: int, height: int, depth: int) -> Model:
        inputs = Input(shape=(height, width, depth))
        x = inputs

        x = keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
        x = keras.layers.MaxPooling2D((2, 2), padding="same")(x)
        x = keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
        x = keras.layers.MaxPooling2D((2, 2), padding="same")(x)
        x = keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
        x = keras.layers.UpSampling2D((2, 2))(x)
        x = keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
        x = keras.layers.UpSampling2D((2, 2))(x)
        x = keras.layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)

        autoencoder = Model(inputs, x, name="autoencoder")
        autoencoder.compile(loss="binary_crossentropy", optimizer='adam')
        return autoencoder
