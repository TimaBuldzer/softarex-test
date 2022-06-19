from django.core.management import BaseCommand
import keras
import numpy as np
import cv2

from apps.autoencoder.helpers.create_dataset import create_dataset
from apps.autoencoder.types import Dimensions


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='Path to saved model')
        parser.add_argument('directory', type=str, help='Absolute path base directory for data')

    def handle(self, *args, **options):
        autoencoder = keras.models.load_model(options['model'])

        dimensions = Dimensions(420, 540)
        dataset = create_dataset(options['directory'], dimensions)
        decoded = autoencoder.predict(dataset.test_x)
        outputs = None

        for i in range(0, 8):
            original = (dataset.test_x[i] * 255).astype("uint8")
            recon = (decoded[i] * 255).astype("uint8")
            print(original.shape)
            print(recon.shape)
            output = np.hstack([original, recon])

            if outputs is None:
                outputs = output

            else:
                outputs = np.vstack([outputs, output])

        # save the outputs image to disk and display it
        cv2.imwrite('apps/autoencoder/data/output.png', outputs)
