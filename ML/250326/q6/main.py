import preprocess as pre
import model as md
import numpy as np
from sklearn.metrics import silhouette_score

def silhouette_calculator(X, cluster):
    
    # 군집화 결과에 대한 silhouette score를 계산합니다.
    # <TODO> dictionary 형태에서 value들을 추출해서 리스트 형태로 변환해 줍니다.
    silhouette = silhouette_score(X, list(cluster.values()))
    
    return silhouette

# <TODO> 여러분이 답으로 제출하고 싶은 군집의 개수로 your_choice 함수의 '?' 부분에 넣은 후 제출하세요.
def your_choice(X):
    
    return md.KMeans(K = 2).fit(X)


def main():
	
    X = pre.load_data()
    
    # <TODO> KMeans의 K에 군집의 개수를 입력해 여러가지 군집화 모델을 시도해보세요.
    Kmeans = your_choice(X)
    
    # <ToDo>: 모델 학습의 결과로 silhouette 값을 계산합니다.
    silhouette = silhouette_calculator(X, Kmeans.cluster)
    
    # 군집의 개수와 silhouette 값을 출력합니다. 
    print('K = {}, silhouette 값: {}'.format(Kmeans, silhouette))
                

if __name__ == "__main__":
    main()