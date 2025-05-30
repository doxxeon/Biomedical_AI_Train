# CNN 생성에 필요한 Keras 라이브러리, 패키지
import os

import tensorflow as tf
from keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator


def create_classifier():
    classifier = Sequential()
    classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation="relu"))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    classifier.add(Conv2D(32, (3, 3), activation="relu"))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    classifier.add(Flatten())
    classifier.add(Dense(units=128, activation="relu"))
    classifier.add(Dense(units=1, activation="sigmoid"))
    classifier.compile(
        optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
    )
    return classifier


def generate_dataset(rescale_ratio, horizontal_flip):
    train_datagen = ImageDataGenerator(
        rescale=rescale_ratio, horizontal_flip=horizontal_flip
    )

    test_datagen = ImageDataGenerator(rescale=rescale_ratio)

    training_set = train_datagen.flow_from_directory(
        "dataset/training_set", target_size=(64, 64), batch_size=2, class_mode="binary"
    )

    test_set = test_datagen.flow_from_directory(
        "dataset/test_set", target_size=(64, 64), batch_size=2, class_mode="binary"
    )

    return train_datagen, test_datagen, training_set, test_set


def main():
    classifier = create_classifier()

    """지시사항 1. `rescale_ratio`의 값을 설정하세요. """
    rescale_ratio = None

    """지시사항 2. `horizontal_flip`을 사용하도록 설정하세요. """
    horizontal_flip = None

    """지시사항 3. 전처리된 훈련 및 테스트 데이터 전처리기 및 데이터셋을 생성하세요. """
    train_datagen, test_datagen, training_set, test_set = None

    classifier.fit_generator(
        training_set,
        steps_per_epoch=10,
        epochs=10,
        validation_data=test_set,
        validation_steps=10,
    )

    output = classifier.predict_generator(test_set, steps=5)
    print(test_set.class_indices)

    return rescale_ratio, horizontal_flip, train_datagen, test_datagen, training_set, test_set, classifier, output


if __name__ == "__main__":
    main()
