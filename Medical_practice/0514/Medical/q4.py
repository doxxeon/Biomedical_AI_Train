import tensorflow as tf
from tensorflow import keras

def VGG16():
    # Sequential 모델 선언
    model = keras.Sequential()

    """
    지시사항 1번
    3 x 3 convolution만을 사용하여 VGG16 Net을 완성하세요.
    """
    # 첫 번째 Conv Block
    # 입력 Shape는 ImageNet 데이터 세트의 크기와 같은 RGB 영상 (224 x 224 x 3)입니다.
    model.add(
        keras.layers.Conv2D(
            filters=64,
            kernel_size=3,
            activation=tf.nn.relu,
            padding="same",
            input_shape=(224, 224, 3),
        )
    )
    model.add(
        keras.layers.Conv2D(
            filters=64, kernel_size=3, activation=tf.nn.relu, padding="same"
        )
    )
    model.add(keras.layers.MaxPooling2D(pool_size=2, strides=2))

    # 두 번째 Conv Block
    model.add(
        keras.layers.Conv2D(
            filters=128, kernel_size=3, activation=tf.nn.relu, padding="same"
        )
    )
    model.add(
        keras.layers.Conv2D(
            filters=128, kernel_size=3, activation=tf.nn.relu, padding="same"
        )
    )
    model.add(keras.layers.MaxPooling2D(pool_size=2, strides=2))

    # 세 번째 Conv Block
    # 위의 코드와 문항 설명의 VGG16 모델 구조를 참고하여 코드를 완성하세요.
    model.add(keras.layers.Conv2D(None))
    model.add(keras.layers.Conv2D(None))
    model.add(keras.layers.Conv2D(None))
    model.add(keras.layers.MaxPooling2D(pool_size=2, strides=2))

    # 네 번째 Conv Block
    # 위의 코드와 문항 설명의 VGG16 모델 구조를 참고하여 코드를 완성하세요.
    model.add(keras.layers.Conv2D(None))
    model.add(keras.layers.Conv2D(None))
    model.add(keras.layers.Conv2D(None))
    model.add(keras.layers.MaxPooling2D(pool_size=2, strides=2))

    # 다섯 번째 Conv Block
    model.add(
        keras.layers.Conv2D(
            filters=512, kernel_size=3, activation=tf.nn.relu, padding="same"
        )
    )
    model.add(
        keras.layers.Conv2D(
            filters=512, kernel_size=3, activation=tf.nn.relu, padding="same"
        )
    )
    model.add(
        keras.layers.Conv2D(
            filters=512, kernel_size=3, activation=tf.nn.relu, padding="same"
        )
    )
    model.add(keras.layers.MaxPooling2D(pool_size=2, strides=2))

    # Fully Connected Layer
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(4096, activation=tf.nn.relu))
    model.add(keras.layers.Dense(4096, activation=tf.nn.relu))
    model.add(keras.layers.Dense(1000, activation=tf.nn.softmax))

    return model


vgg16 = VGG16()
vgg16.summary()
