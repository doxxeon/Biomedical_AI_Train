import os
import tensorflow as tf
from tensorflow.keras import layers, models, Sequential
from tensorflow.keras.datasets import mnist
import numpy as np

def load_data(): # 학습에 사용할 데이터입니다.

    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    
    X_train, X_test = X_train / 255.0, X_test / 255.0
    
    X_train = np.expand_dims(X_train, axis=-1)
    X_test = np.expand_dims(X_test, axis=-1)
    
    return X_train, X_test, y_train, y_test

def main():
    X_train, X_test, y_train, y_test = load_data() # 빠른 실습을 위해 양이 적은 X_test, y_test 를 학습합니다.
    
    # TODO: 10번째 체크포인트의 경로를 checkpnt_path에 저장하세요
    checkpnt_path = '/Users/kimdohyeon/건양대학교병원_바이오헬스/Biomedical_AI_Train/DL/250423/q3/checkpoints/cp-0010.ckpt'
    
    # TODO: 불러온 체크포인트를 불러와 model에 저장하세요
    model = tf.keras.models.load_model(checkpnt_path)
    
    # TODO: 10epoch까지 학습된 이 모델을 11번째 epoch부터 이어서 5 epoch 더 학습시키세요
    hist = model.fit( x=X_test, y=y_test, batch_size=64, epochs=15,
        shuffle=True, initial_epoch=11)
        
    return hist, checkpnt_path

if __name__ == "__main__":
    main()
