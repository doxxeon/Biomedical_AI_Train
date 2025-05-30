import warnings, logging, os
logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


import tensorflow as tf
from tensorflow.keras import layers, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.resnet50 import ResNet50

import numpy as np
from Avoid_overfitting.q4.preprocess import *

def load_transfer_model():
    # ImageNet으로 훈련된 ResNet-50 모델을 불러옵니다.
    # 가장 마지막의 classification layer는 포함하지 않습니다. 
    base_model = ResNet50(input_shape=(96, 96, 3), include_top=False, weights='imagenet')
    
    # TODO: [지시사항 1번] 모델이 학습되지 않도록 설정하세요.
    None
    
    # TODO: [지시사항 2번] 지시사항에 따라 layer를 추가하세요.
    transfer_model = Sequential([
        layers.UpSampling2D(size=(3, 3), interpolation='bilinear'),
        None
    ])

    return transfer_model

def main(transfer_model=None, epochs=3):
    # 채점을 위한 코드입니다. 수정하지 마세요!
    np.random.seed(81)
    
    num_classes = 10
    x_train, y_train, x_test, y_test = cifar10_data(num_classes)
    x_train, y_train, x_test, y_test = x_train[:5000], y_train[:5000], x_test[:100], y_test[:100]
    
    if transfer_model is None:
        transfer_model = load_transfer_model()
    
    # [지시사항 3번] 모델 학습을 위한 Optimizer, loss 함수, 평가 지표를 설정하세요.
    optimizer = None
    None
    
    # 모델을 학습시킵니다.
    hist = transfer_model.fit(x_train, y_train, epochs=3, batch_size=500)
    
    # 완성된 모델을 확인해봅니다.
    print()
    transfer_model.summary()
    
    # 테스트 데이터로 모델 성능을 확인합니다.
    loss, accuracy = transfer_model.evaluate(x_test, y_test)
    
    print('\n훈련된 모델의 테스트 정확도는 {:.3f}% 입니다.\n'.format(accuracy * 100))
    
    return optimizer, hist

if __name__ == "__main__":
    main()