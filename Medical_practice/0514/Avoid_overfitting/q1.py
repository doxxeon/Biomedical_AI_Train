import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras import layers, Sequential, Input
from tensorflow.keras.datasets import fashion_mnist

# Fashion MNIST 데이터셋을 불러옵니다.
def load_mnist():
    (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
    
    # 이미지의 픽셀값을 0과 1 사이로 정규화합니다.
    X_train, X_test = X_train / 255.0, X_test / 255.0

    return X_train, X_test, y_train, y_test

def build_mlp_model(img_shape):
    model = Sequential()

    model.add(Input(shape=img_shape))
    
    # TODO: [지시사항 1번] 기본 MLP 모델을 만드세요.
    model.add(layers.Flatten(input_shape=img_shape))
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))

    return model

def build_bn_mlp_model(img_shape):
    model = Sequential()

    model.add(Input(shape=img_shape))
    
    # TODO: [지시사항 2번] Batch Normalizatino이 추가된 MLP 모델을 만드세요.
    model.add(layers.Flatten(input_shape=img_shape))
    model.add(layers.Dense(1024))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.Dense(256))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.Dense(10, activation='softmax'))

    return model

# 각 모델의 hyperparameter를 설정하고 학습합니다.
def run_model(model, X_train, X_test, y_train, y_test, epochs=5):
    model.compile(optimizer="sgd", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    hist = model.fit(X_train, y_train, epochs=epochs, batch_size=64, shuffle=True, verbose=2)

    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

    return hist, test_loss, test_acc

def main():
    tf.random.set_seed(2022)

    X_train, X_test, y_train, y_test = load_mnist()
    img_shape = X_train[0].shape

    mlp_model = build_mlp_model(img_shape)
    bn_mlp_model = build_bn_mlp_model(img_shape)

    print("=" * 25, "[기본 MLP 학습]", "=" * 25)
    _, mlp_loss, mlp_acc = run_model(mlp_model, X_train, X_test, y_train, y_test)
    
    print()
    print("=" * 25, "[BN 추가된 MLP 학습]", "=" * 25)
    _, bn_mlp_loss, bn_mlp_acc = run_model(bn_mlp_model, X_train, X_test, y_train, y_test)

    print()
    print("=" * 25, "결과", "=" * 25)
    print("[기본 MLP] 테스트 Loss: {:.5f}, 테스트 정확도: {:.3f}%".format(mlp_loss, mlp_acc * 100))
    print("[BN 추가된 MLP] 테스트 Loss: {:.5f}, 테스트 정확도: {:.3f}%".format(bn_mlp_loss, bn_mlp_acc * 100))

if __name__ =="__main__":
    main()