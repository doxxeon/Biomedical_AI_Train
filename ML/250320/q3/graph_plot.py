import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def svm_model_plot(trained_svm, feature, label, feature_name):
    
    x1_min = min(feature[:, 0]) -1
    x1_max = max(feature[:, 0]) +1
    x2_min = min(feature[:, 1]) -1
    x2_max = max(feature[:, 1]) +1
    XX, YY = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]
    
    levels = [-1, 0, 1]
    linestyles = ['dashed', 'solid', 'dashed']
    Z = trained_svm.decision_function(np.c_[XX.ravel(), YY.ravel()])
    Z = Z.reshape(XX.shape)
    
    plt.contour(XX, YY, Z, levels, colors='k', linestyles=linestyles)
    plt.scatter(trained_svm.support_vectors_[:, 0], trained_svm.support_vectors_[:, 1], s=120, linewidth=4)
    plt.scatter(feature[:, 0], feature[:, 1], c=label, s=60, linewidth=1, cmap=plt.cm.Paired)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    
    plt.xlabel(feature_name[0])
    plt.ylabel(feature_name[1])
    
    plt.savefig("result3.png")