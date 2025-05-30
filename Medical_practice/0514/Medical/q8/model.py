import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow.keras import optimizers
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import vgg
from elice_utils import EliceUtils

elice_utils = EliceUtils()


dir_loc = "dataset/"
dir_training = "training_set"
dir_test = "test_set"
classNames = os.listdir("./" + dir_loc + dir_test)  # 각 클래스의 이름들
numClass = len(classNames)
image_size = 64
batch_size = 64


def generate_model():
    model = vgg.VGG19(input_shape=(image_size, image_size, 1))
    model.add(Dense(numClass, activation="softmax"))
    model.compile(
        loss="categorical_crossentropy",
        optimizer=optimizers.RMSprop(lr=1e-4),
        # optimizer=optimizers.Adam(lr=1e-4),
        metrics=["acc"],
    )

    # 새로운 모델 요약
    model.summary()
    return model


def generate_imgset(tr_loc, te_loc):
    # Training_set을 생성
    train_datagen = ImageDataGenerator(
        rescale=1 / 255,
        rotation_range=3,
        width_shift_range=0.01,
        height_shift_range=0.10,
        zoom_range=0.05,
        fill_mode="nearest",
    )
    training_set = train_datagen.flow_from_directory(
        tr_loc,
        target_size=(64, 64),
        batch_size=2,
        color_mode="grayscale",
        class_mode="categorical",
    )

    # test_set을 생성
    test_datagen = ImageDataGenerator(rescale=1.0 / 255)
    test_set = test_datagen.flow_from_directory(
        te_loc,
        target_size=(64, 64),
        batch_size=2,
        color_mode="grayscale",
        class_mode="categorical",
    )
    return training_set, test_set


def train_model(model, training_set, val_set):
    result = model.fit(
        training_set,
        steps_per_epoch=20,
        epochs=30,
        validation_data=val_set,
        validation_steps=10,
    )
    #       [참고] validation data가 없으므로 test_set으로 임의 대체하였습니다.
    return result, model


def main():
    model = generate_model()
    training_set, test_set = generate_imgset(dir_loc + dir_training, dir_loc + dir_test)
    result, model = train_model(model, training_set, test_set)


if __name__ == "__main__":
    main()
