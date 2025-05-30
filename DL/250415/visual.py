import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from visual import *

from sklearn.neural_network import MLPClassifier

def visualize(clf, X, Y):
    X_ = []
    Y_ = []
    colors = []
    shapes = []

    plt.figure(figsize=(6, 6))

    for x, y in zip(X, Y):
        X_.append(x[1])
        Y_.append(x[0])
        if y == 0:
            colors.append('b')
        else:
            colors.append('r')

        if clf.predict([x])[0] == y:
            shapes.append('o')
        else:
            shapes.append('x')

    for x, y in zip(X, Y):
        c = '#87CEFA'
        if clf.predict([x])[0] == 1:
            c = '#fab387'
        plt.scatter(x[1], x[0], marker='s', c=c, s=1200, edgecolors='none')

    for _s, c, _x, _y in zip(shapes, colors, X_, Y_):
        plt.scatter(_x, _y, marker=_s, c=c, s=200)
    plt.savefig("image.svg", format="svg")
    plt.show()
