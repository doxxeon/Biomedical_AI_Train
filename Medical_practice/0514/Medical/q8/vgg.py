import datetime

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from tensorflow.keras.models import Sequential

from elice_utils import EliceUtils

elice_utils = EliceUtils()

K.clear_session()  # 새로운 세션으로 시작


class VGG19(Sequential):
    def __init__(self, input_shape):
        super().__init__()

        self.add(
            Conv2D(
                64,
                kernel_size=(7, 7),
                padding="same",
                activation="relu",
                input_shape=input_shape,
            )
        )
        self.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        self.add(Conv2D(128, kernel_size=(5, 5), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        self.add(Conv2D(256, kernel_size=(3, 3), padding="same", activation="relu"))
        self.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        self.add(Flatten())
        self.add(Dense(64, activation="relu"))

        self.compile(
            optimizer=tf.keras.optimizers.Adam(0.003),
            loss="categorical_crossentropy",
            metrics=["accuracy"],
        )


if __name__ == "__main__":
    main()
