# 패키지 불러오기
import os

import numpy as np
import tensorflow as tf
from tensorflow.keras import optimizers
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from elice_utils import EliceUtils
import vgg

elice_utils = EliceUtils()


def generate_model(numClass):
    """
    지시사항 1. VGG 모델의 입력 이미지 사이즈를 224x224로 변경해주세요
    """
    model = vgg.VGG19(input_shape=(None, None, 3))

    model.add(Dense(numClass, activation="softmax"))
    model.compile(
        loss="categorical_crossentropy",
        optimizer=optimizers.RMSprop(lr=1e-3),
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

    """
    지시사항 2. 학습 및 테스트 이미지의 크기를 224x224로 변경해주세요.
    """

    training_set = train_datagen.flow_from_directory(
        tr_loc, target_size=None, batch_size=2, class_mode="categorical"
    )

    # test_set을 생성
    test_datagen = ImageDataGenerator(rescale=1.0 / 255)
    test_set = test_datagen.flow_from_directory(
        te_loc, target_size=None, batch_size=2, class_mode="categorical"
    )
    return training_set, test_set


def train_model(model, training_set, val_set):
    """
    지시사항 3. model을 training data에 맞게 fit()합니다.
    """

    result = model.fit(None, steps_per_epoch=None, epochs=None, validation_data=None)
    return result, model


def main():
    dir_loc = "dataset/"
    dir_training = "training_set"
    dir_test = "test_set"
    classNames = os.listdir("./" + dir_loc + dir_test)  # 각 클래스의 이름들
    numClass = len(classNames)

    batch_size = 64

    model = generate_model(numClass)
    training_set, test_set = generate_imgset(dir_loc + dir_training, dir_loc + dir_test)

    result, model = train_model(model, training_set, test_set)


if __name__ == "__main__":
    main()
