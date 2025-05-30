import os

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import auc, confusion_matrix, roc_curve
from sklearn.preprocessing import label_binarize

import model as md
import result as rs


dir_loc = "dataset/"
dir_training = "training_set"
dir_test = "test_set"
classNames = os.listdir("./" + dir_loc + dir_test)  # 각 클래스의 이름들
numClass = len(classNames)
image_size = 64
batch_size = 64


def one_hot(l):
    temp_list = list()
    for i in l:
        if i == 0:
            temp_list.append([1, 0])
        else:
            temp_list.append([0, 1])
    return np.array(temp_list)


def main():
    model = md.generate_model()
    training_set, test_set = md.generate_imgset(
        dir_loc + dir_training, dir_loc + dir_test
    )
    result, model = md.train_model(model, training_set, test_set)

    y_pred, y_test, acc, cm, df_cm = rs.get_result(model, training_set, test_set)
    y_pred = one_hot(label_binarize(y_pred, classes=[0, 1]))
    y_test = one_hot(label_binarize(y_test, classes=[0, 1]))
    generate_roc(y_pred, y_test)
    return y_pred, y_test


def generate_roc(y_pred, y_test):
    # 각 클래스의 ROC Curve 값을 계산하여 넣어 줄 변수를 선언합니다.
    fpr = dict()
    tpr = dict()
    roc_auc = dict()

    for i in range(numClass):
        fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_pred[:, i])
        
        """
        지시사항 1. auc() 함수에 fpr[i], tpr[i]를 인자로 넣어 각각의 클래스에서의 ROC & AUC 값을 획득하세요.
        """
        roc_auc[i] = auc(None, None)

    temp_cls = list()
    for nth_class in range(numClass):
        temp_cls.append(plot_ROC_curve(fpr, tpr, roc_auc, nth_class))

    return numClass, fpr, tpr, roc_auc, temp_cls


# ROC curve를 그리기 위해 사용되는 함수입니다.
def plot_ROC_curve(fpr, tpr, roc_auc, nth_class):

    plt.figure()
    lw = 2

    color_name = ""

    """
    지시사항 2. 각 클래스에서의 분류가 잘 되었는지 확인하기 위해 class에 따라 별도의 색을 지정합니다.
    nth_class의 인자가 normal(0)인 경우 color_name을 'red'로 선언합니다.
    그 외의 경우, color_name을 'orange'로 선언합니다.
    """
    if nth_class == 0:
        None
    else:
        None

    plt.plot(
        fpr[nth_class],
        tpr[nth_class],
        color=color_name,
        lw=lw,
        label="ROC curve (area = %0.2f)" % roc_auc[nth_class],
    )
    plt.plot([0, 1], [0, 1], color="green", lw=lw, linestyle="--")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Class %s ROC(Receiver Operating Characteristic) Curve" % nth_class)
    plt.legend(loc="lower right")
    plt.savefig("roc curve.png")

    return color_name


if __name__ == "__main__":
    y_pred, y_test = main()
