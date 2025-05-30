import tensorflow as tf
from tensorflow.keras import layers, Sequential

# TODO: [지시사항 1번] 지시사항 대로 Conv2D 하나로 이루어진 모델을 완성하세요 
def build_model1(input_shape):
    model = layers.Conv2D(filters=1, kernel_size=(3,3), strides=(1,1), padding="same",
                          activation="relu", 
                          input_shape=input_shape[1:])
    
    return model

# TODO: [지시사항 2번] 지시사항 대로 Conv2D 두개로 이루어진 모델을 완성하세요 
def build_model2(input_shape):
    model = Sequential([layers.Conv2D(filters=4, kernel_size=(3,3),strides=(1,1), padding='same', input_shape=input_shape[1:]),
                        layers.Conv2D(filters=4, kernel_size=(3,3), strides=(1,1), padding='same')])
    
    return model

# TODO: [지시사항 3번] 지시사항 대로 Conv2D 세개로 이루어진 모델을 완성하세요 
def build_model3(input_shape):
    model = Sequential()
    
    model.add(layers.Conv2D(filters=2, kernel_size=(3,3), strides=(1,1), padding='same', input_shape=input_shape[1:]))
    model.add(layers.Conv2D(filters=4, kernel_size=(3,3), strides=(1,1), padding='same'))
    model.add(layers.Conv2D(filters=8, kernel_size=(3,3), strides=(1,1)))
    
    return model

def main():
    input_shape = (1, 5, 5, 1)
    
    model1 = build_model1(input_shape)
    model2 = build_model2(input_shape)
    model3 = build_model3(input_shape)

    x = tf.ones(input_shape)
    print("model1을 통과한 결과:", model1(x).shape)
    print("model2을 통과한 결과:", model2(x).shape)
    print("model3을 통과한 결과:", model3(x).shape)

if __name__=="__main__":
    main()
