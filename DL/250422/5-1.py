import tensorflow as tf
import numpy as np
from tensorflow.keras import layers

np.random.seed(100)
def generate_data(batch_size, n_steps):
    freq1, freq2, offsets1, offsets2 = np.random.rand(4,batch_size,1)
    time = np.linspace(0, 1, n_steps)
    series = 0.5 * np.sin((time - offsets1)*(freq1 * 10 + 10))
    series += 0.1 * np.sin((time - offsets2)*(freq2 * 10 + 10))
    series += 0.1 * (np.random.rand(batch_size,n_steps) - 0.5)
    return series[...,np.newaxis].astype(np.float32)

def make_model(n_step):
    model = tf.keras.models.Sequential()
    model.add(layers.Flatten(input_shape= [n_step,]))
    model.add(layers.Dense(1))
    model.compile(optimizer = 'adam', loss = 'mse')
    return model

n_step = 50
series = generate_data(10000, n_step +1)
x_train, y_train = series[:7000, :n_step],series[:7000,-1]
x_val, y_val = series[7000:9000, :n_step],series[7000:9000,-1]
x_test, y_test = series[9000:, :n_step],series[9000:,-1]

# 모델 구성
fcl_model = make_model(n_step)

# TODO: 지시사항을 보고 fit 함수의 매개변수를 설정하세요
hist=fcl_model.fit(
x=x_train, y=y_train, batch_size=100, epochs=20, verbose=2,shuffle=None,
validation_data=(x_val, y_val),  initial_epoch=11,
validation_steps=10, validation_batch_size=50, validation_freq=5)
