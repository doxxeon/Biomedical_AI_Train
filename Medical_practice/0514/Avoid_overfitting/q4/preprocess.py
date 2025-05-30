import warnings, logging, os
logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
import pickle


def cifar10_data(num_classes):
    '''
    CIFAR10 데이터셋을 불러온 뒤, 전처리 작업을 수행합니다.
    '''
    root = 'data/data_batch_'
    x_train = []
    y_train = []
    for i in range(1, 2):
        with open(root + str(i), mode='rb') as file:
            batch = pickle.load(file, encoding='latin1')
            if i == 1:
                x_train = batch['data'].reshape((len(batch['data']), 3, 32, 32)).transpose(0, 2, 3, 1).astype(np.float32)
                y_train = np.array(batch['labels']).astype(np.float32)
            else:
                x_train = np.concatenate((batch['data'].reshape((len(batch['data']), 3, 32, 32)).transpose(0, 2, 3, 1).astype(np.float32), x_train))
                y_train = np.concatenate((np.array(batch['labels']).astype(np.float32), y_train))

    x_train /= 255
    y_train = keras.utils.to_categorical(y_train, num_classes)

    root = 'data/test_batch'
    with open(root, mode='rb') as file:
        batch = pickle.load(file, encoding='latin1')
        x_test = batch['data'].reshape((len(batch['data']), 3, 32, 32)).transpose(0, 2, 3, 1).astype(np.float32)
        y_test = np.array(batch['labels']).astype(np.float32)

        x_test /= 255
        y_test = keras.utils.to_categorical(y_test, num_classes)
    
    return x_train, y_train, x_test, y_test