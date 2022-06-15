from os import listdir
from os.path import isfile, join
from typing import Iterable

import cv2
import numpy as np

height = int
width = int


def create_dataset(directory: str,
                   dimensions: tuple[height, width]) -> Iterable:  # TODO: change 'Iterable' into exact type :)
    image_paths = [f for f in listdir(directory) if isfile(join(directory, f))]

    data = []
    for imagePath in image_paths:
        image = cv2.imread(directory + imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (dimensions[0], dimensions[1]))
        data.append(image)
    data = np.expand_dims(data, axis=-1)
    data = np.array(data, dtype="float32") / 255.0
    return data
