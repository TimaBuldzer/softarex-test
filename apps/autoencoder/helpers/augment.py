from keras.preprocessing.image import ImageDataGenerator
import numpy as np

from apps.autoencoder.helpers.create_dataset import create_dataset

width = int
height = int


def augment_data(
        directory: str,
        dimensions: tuple[height, width],
        quantity: int = 50,
        img_format: str = 'png') -> None:
    datagen = ImageDataGenerator(
        rotation_range=40,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        brightness_range=(0.5, 1.5))

    dataset = create_dataset(directory, dimensions)

    array = np.array(dataset)

    for _ in range(quantity):
        datagen.flow(
            array, batch_size=16,
            save_to_dir=directory,
            save_prefix='dr',
            save_format=img_format
        )
