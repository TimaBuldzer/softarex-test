from autoencoder.autoencoder import Autoencoder
from autoencoder.helpers.create_dataset import create_dataset
from sklearn.model_selection import train_test_split

from autoencoder.types import Dimensions

train_path = '/content/train'
test_path = '/content/test'
epochs = 12
batch_size = 8

dimensions = Dimensions(420, 540)

dataset = create_dataset('/content/', dimensions)

x_train, x_valid, y_train, y_valid = train_test_split(dataset.train_x, dataset.train_y, test_size=0.1, random_state=111)

autoencoder = Autoencoder.build(dimensions)

H = autoencoder.fit(
    x_train, y_train,
    epochs=epochs,
    batch_size=batch_size,
    validation_data=(x_valid, y_valid)
)

autoencoder.save('autoencoder')
