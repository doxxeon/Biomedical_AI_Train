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

    model.add(layers.SimpleRNN(20, return_sequences = True, input_shape = [None, 1])) 
    model.add(layers.SimpleRNN(20))
    model.add(layers.Dense(1))

    model.compile(optimizer = 'adam', loss = 'mse')
    return model

n_step = 50
series = generate_data(10000, n_step +1)
x_train, y_train = series[:7000, :n_step],series[:7000,-1]
x_val, y_val = series[7000:9000, :n_step],series[7000:9000,-1]
x_test, y_test = series[9000:, :n_step],series[9000:,-1]

logs = "logs"
tb = tf.keras.callbacks.TensorBoard(log_dir=logs)

e = 20 #제거 혹은 변경 금지
def main():        
    deep_rnn = make_model(n_step)
    hist=deep_rnn.fit(
    x=x_train, y=y_train, epochs=e,
    validation_data=(x_val, y_val),validation_freq=2,callbacks=[tb]) # TODO: 정의한 콜백함수를 리스트로 묶어 전달하세요
if __name__ == "__main__":
    main()
