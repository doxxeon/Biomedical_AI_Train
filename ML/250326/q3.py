import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs


"""
1. 지시 사항과 동일한 타원형 분포의 데이터를
   생성합니다.
"""
# make_blobs()으로 데이터를 생성해보세요.
X, y = make_blobs(n_samples=300, n_features=2, centers=3, cluster_std=0.8, random_state=0)

# 데이터의 분포를 변형시키기 위해 transformation을 진행합니다.
transformation = [[0.60834549, -0.63667341],[-0.40887718,0.85253229]]
X_aniso = np.dot(X, transformation)

# 데이터 프레임 만들기 
clusterDF = pd.DataFrame(data = X_aniso, columns= ['ftr1','ftr2'])
clusterDF['target'] = y
target_list = np.unique(y)

# 생성된 데이터 시각화
def data_visualize():
    fig, ax = plt.subplots()
    plt.title('data')
    
    for target in target_list:
        target_cluster = clusterDF[clusterDF['target'] == target]
        ax.scatter(x = target_cluster['ftr1'], y = target_cluster['ftr2'])
    
    fig.savefig("q3_plot.png")
    
    
"""
2. K-Means 클러스터링을 수행하여
   클러스터링 결과를 데이터 프레임 내에 
   저장하는 함수를 완성합니다.
"""
def K_means():
    
    k_means = KMeans(n_clusters=3, random_state=0)
    
    kmeans_label = k_means.fit_predict(clusterDF.drop(['target'], axis=1))
    
    clusterDF['kmeans_label']=kmeans_label
    
    # Kmeans 군집의 중심값을 뽑아 저장합니다.
    center = k_means.cluster_centers_
    
    # KMeans 군집 결과를 시각화합니다.
    unique_labels = np.unique(kmeans_label)
    fig, ax = plt.subplots()
    plt.title('K-Means')
    
    for label in unique_labels:
        label_cluster = clusterDF[clusterDF['kmeans_label'] == label]
        center_x_y = center[label]
        ax.scatter(x = label_cluster['ftr1'], y = label_cluster['ftr2'])
        ax.scatter(x = center_x_y[0], y = center_x_y[1], s = 70,color = 'k', marker = '$%d$' % label)
    
    fig.savefig("q3_kmeans_plot.png")

    print("K-means Clustering")
    print(clusterDF.groupby('target')['kmeans_label'].value_counts())
    
    return kmeans_label
    
"""
3. GMM 클러스터링을 수행하여
   클러스터링 결과를 데이터 프레임 내에 
   저장하는 함수를 완성합니다.
"""
def GMM():
    
    gmm = GaussianMixture(n_components=3, random_state=0)
    
    gmm_label = gmm.fit_predict(clusterDF.drop(['target'], axis=1))
    
    clusterDF['gmm_label']=gmm_label
    
    unique_labels = np.unique(gmm_label)
    
    # GMM 군집 결과를 시각화합니다.
    fig, ax = plt.subplots()
    plt.title('GMM')
    
    for label in unique_labels:
        label_cluster = clusterDF[clusterDF['gmm_label'] == label]
        plt.scatter(x = label_cluster['ftr1'], y = label_cluster['ftr2'])
    
    fig.savefig("q3_gmm_plot.png")
    
    print("Gaussian Mixture Model")
    print(clusterDF.groupby('target')['gmm_label'].value_counts())
    
    return gmm_label

def main():
    data_visualize()
    K_means()
    GMM()

if __name__ == "__main__":
    main()
