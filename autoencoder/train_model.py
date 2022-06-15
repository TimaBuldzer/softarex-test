from autoencoder.autoencoder import Autoencoder
from autoencoder.helpers.create_dataset import create_dataset

train_path = '/content/train'
test_path = '/content/test'
width = 420
height = 540
depth = 1
epochs = 10
batch_size = 8
trainX = create_dataset(train_path, (height, width))
testX = create_dataset(test_path, (height, width))

autoencoder = Autoencoder().build(height, width, depth)

autoencoder.fit(
    trainX, trainX,
    validation_data=(testX, testX),
    epochs=epochs,
    batch_size=batch_size)

autoencoder.save('autoencoder')
