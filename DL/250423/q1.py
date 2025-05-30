import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras import layers, models, Sequential
from tensorflow.keras.datasets import mnist
import numpy as np

def load_data():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    
    X_train, X_test = X_train / 255.0, X_test / 255.0
    
    X_train = np.expand_dims(X_train, axis=-1)
    X_test = np.expand_dims(X_test, axis=-1)
    
    return X_train, X_test, y_train, y_test

def build_model(input_shape, num_classes=10):
    model = Sequential()
    
    model.add(layers.Conv2D(16, kernel_size=(3, 3), padding="same", activation="relu", input_shape=input_shape))
    model.add(layers.MaxPool2D(2))
    
    model.add(layers.Conv2D(32, kernel_size=(3, 3), padding="same", activation="relu"))
    model.add(layers.MaxPool2D(2))
    
    model.add(layers.Flatten())
    model.add(layers.Dense(num_classes, activation="softmax"))
    
    return model

def main():
    X_train, X_test, y_train, y_test = load_data()
    
    model = build_model(X_train[0].shape)
    
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(X_train, y_train, epochs=1, batch_size=64, shuffle=True, verbose=2)
    
    # TODO: H5 형식으로 모델 저장
    model.save("./h5_model.h5")
    
    # TODO: SavedModel 형식으로 모델 저장
    model.save("./saved_model")

if __name__ == "__main__":
    main()
