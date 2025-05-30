import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
import tensorflow.keras.backend as K
from sklearn.metrics import accuracy_score, confusion_matrix
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import model as md
from elice_utils import EliceUtils

elice_utils = EliceUtils()


dir_loc = "dataset/"
dir_training = "training_set"
dir_test = "test_set"
classNames = os.listdir("./" + dir_loc + dir_test)  # 각 클래스의 이름들
numClass = len(classNames)
image_size = 64
batch_size = 64


def get_result(model, test_set, y_test):
    y_pred = model.predict_generator(test_set, test_set.samples // test_set.batch_size)
    y_pred = np.argmax(y_pred, axis=1)
    y_test = test_set.labels

    print(test_set.class_indices)
    print(y_pred)
    print(y_test)

    acc = accuracy_score(y_pred, y_test) * 100
    print("%.2f" % acc, "%")

    # confusion matrix를 cm으로 선언합니다.
    cm = confusion_matrix(y_test, y_pred)
    df_cm = pd.DataFrame(
        cm, index=[i for i in classNames], columns=[i for i in classNames]
    )

    sn.set(font_scale=1.5)
    plt.figure(figsize=(10, 7))
    sn.heatmap(df_cm, annot=True, fmt="d", cmap="YlGnBu")
    plt.show()
    plt.savefig("graph.png")
    elice_utils.send_image("graph.png")
    plt.rcParams.update(plt.rcParamsDefault)
    K.clear_session()  # 세션 클리어
    return y_pred, y_test, acc, cm, df_cm


def main():
    model = md.generate_model()
    training_set, test_set = md.generate_imgset(
        dir_loc + dir_training, dir_loc + dir_test
    )
    result, model = md.train_model(model, training_set, test_set)

    y_pred, y_test, acc, cm, df_cm = get_result(model, training_set, test_set)


if __name__ == "__main__":
    main()
