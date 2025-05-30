import datetime

import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests
import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow.keras import optimizers
from tensorflow.keras.layers import (
    Conv2D,
    Dense,
    Dropout,
    Flatten,
    Input,
    MaxPool2D,
    MaxPooling2D,
)
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.models import Model, Sequential

K.clear_session()  # 새로운 세션으로 시작
from elice_utils import EliceUtils

elice_utils = EliceUtils()


class VGG19(Sequential):
    def __init__(self, input_shape):
        super().__init__()

        self.add(
            Conv2D(
                64,
                kernel_size=(3, 3),
                padding="same",
                activation="relu",
                input_shape=input_shape,
            )
        )
        self.add(Conv2D(64, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        self.add(Conv2D(128, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(Conv2D(128, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        self.add(Conv2D(256, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(Conv2D(256, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(Conv2D(256, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(Conv2D(256, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        self.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        self.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        self.add(Flatten())
        self.add(Dense(4096, activation="relu"))
        self.add(Dropout(0.5))
        self.add(Dense(4096, activation="relu"))
        self.add(Dropout(0.5))
        # self.add(Dense(1000, activation= 'softmax'))

        self.compile(
            optimizer=tf.keras.optimizers.Adam(0.003),
            loss="categorical_crossentropy",
            metrics=["accuracy"],
        )
