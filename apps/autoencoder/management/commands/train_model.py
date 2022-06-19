from django.core.management import BaseCommand

from apps.autoencoder.autoencoder import Autoencoder
from apps.autoencoder.helpers.create_dataset import create_dataset
from sklearn.model_selection import train_test_split

from apps.autoencoder.autoencoder import Dimensions


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('epochs', type=int, help='Epochs to train model')
        parser.add_argument('directory', type=str, help='Absolute path base directory for data')

    def handle(self, *args, **options):
        epochs = options['epochs']
        batch_size = 8

        dimensions = Dimensions(420, 540)

        dataset = create_dataset(options['directory'], dimensions)

        x_train, x_valid, y_train, y_valid = train_test_split(dataset.train_x, dataset.train_y, test_size=0.1,
                                                              random_state=111)

        autoencoder = Autoencoder.build(dimensions)

        autoencoder.fit(
            x_train, y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=(x_valid, y_valid)
        )

        autoencoder.save('autoencoder')
