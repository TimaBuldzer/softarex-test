import os
import numpy as np

from keras_preprocessing.image import load_img, img_to_array

from autoencoder.types import Dimensions, Dataset


def create_dataset(directory: str, dimensions: Dimensions) -> Dataset:
    train = directory + 'train/'
    train_cleaned = directory + 'train_cleaned/'
    test = directory + 'test/'

    train_images = sorted(os.listdir(train))
    train_labels = sorted(os.listdir(train_cleaned))
    test_images = sorted(os.listdir(test))

    print("Total number of images in the training set: ", len(train_images))
    print("Total number of cleaned images found: ", len(train_labels))
    print("Total number of samples in the test set: ", len(test_images))

    dataset = Dataset(
        train_x=list(),
        train_y=list(),
        test_x=list()
    )

    for img in train_images:
        img = load_img(train + img, grayscale=True, target_size=(dimensions.height, dimensions.width))
        img = img_to_array(img).astype('float32') / 255.
        dataset.train_x.append(img)

    for img in train_labels:
        img = load_img(train_cleaned + img, grayscale=True, target_size=(dimensions.height, dimensions.width))
        img = img_to_array(img).astype('float32') / 255.
        dataset.train_y.append(img)

    for img in test_images:
        img = load_img(test + img, grayscale=True, target_size=(dimensions.height, dimensions.width))
        img = img_to_array(img).astype('float32') / 255.
        dataset.test_x.append(img)

    dataset.train_x = np.array(dataset.train_x)
    dataset.train_y = np.array(dataset.train_y)
    dataset.test_x = np.array(dataset.test_x)

    return dataset
