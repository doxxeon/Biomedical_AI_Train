import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def svm_model_plot(linear_svm, poly_svm, rbf_svm, sig_svm, feature, label, feature_name):
    
    x1_min = min(feature[:, 0]) -1
    x1_max = max(feature[:, 0]) +1
    x2_min = min(feature[:, 1]) -1
    x2_max = max(feature[:, 1]) +1
    XX, YY = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]
    
    levels = [-1, 0, 1]
    linestyles = ['dashed', 'solid', 'dashed']
    
    # for linear
    
    Z = linear_svm.decision_function(np.c_[XX.ravel(), YY.ravel()])
    Z = Z.reshape(XX.shape)
    
    plt.subplot(2, 2, 1)
    plt.contour(XX, YY, Z, levels, colors='k', linestyles=linestyles)
    plt.scatter(linear_svm.support_vectors_[:, 0], linear_svm.support_vectors_[:, 1], s=120, linewidth=4)
    plt.scatter(feature[:, 0], feature[:, 1], c=label, s=60, linewidth=1, cmap=plt.cm.Paired)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    
    plt.xlabel(feature_name[0])
    plt.ylabel(feature_name[1])
    plt.title('Linear Kernel')
    
    # for poly
    
    Z2 = poly_svm.decision_function(np.c_[XX.ravel(), YY.ravel()])
    Z2 = Z2.reshape(XX.shape)
    
    plt.subplot(2, 2, 2)
    plt.contour(XX, YY, Z2, levels, colors='k', linestyles=linestyles)
    plt.scatter(poly_svm.support_vectors_[:, 0], poly_svm.support_vectors_[:, 1], s=120, linewidth=4)
    plt.scatter(feature[:, 0], feature[:, 1], c=label, s=60, linewidth=1, cmap=plt.cm.Paired)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    
    plt.xlabel(feature_name[0])
    plt.ylabel(feature_name[1])
    plt.title('Poly Kernel')
    
    # for rbf
    
    Z3 = rbf_svm.decision_function(np.c_[XX.ravel(), YY.ravel()])
    Z3 = Z3.reshape(XX.shape)
    
    plt.subplot(2, 2, 3)
    plt.contour(XX, YY, Z3, levels, colors='k', linestyles=linestyles)
    plt.scatter(rbf_svm.support_vectors_[:, 0], rbf_svm.support_vectors_[:, 1], s=120, linewidth=4)
    plt.scatter(feature[:, 0], feature[:, 1], c=label, s=60, linewidth=1, cmap=plt.cm.Paired)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    
    plt.xlabel(feature_name[0])
    plt.ylabel(feature_name[1])
    plt.title('RBF Kernel')
    
    # for sigmoid
    
    Z4 = sig_svm.decision_function(np.c_[XX.ravel(), YY.ravel()])
    Z4 = Z4.reshape(XX.shape)
    
    plt.subplot(2, 2, 4)
    plt.contour(XX, YY, Z4, levels, colors='k', linestyles=linestyles)
    plt.scatter(sig_svm.support_vectors_[:, 0], sig_svm.support_vectors_[:, 1], s=120, linewidth=4)
    plt.scatter(feature[:, 0], feature[:, 1], c=label, s=60, linewidth=1, cmap=plt.cm.Paired)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    
    plt.xlabel(feature_name[0])
    plt.ylabel(feature_name[1])
    plt.title('Sigmoid Kernel')
    
    plt.tight_layout()
    
    plt.savefig("result4.png")