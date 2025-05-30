import preprocess as pre
import model as md
import numpy as np


def variance_calculator(model,X):
    
    # PCA 결과에 대한 분산의 유지율 계산하여 반환합니다.
    # <ToDo>: 원본의 분산을 구합니다.
    original_var = (X.var(axis=0)).sum()
    
    # <ToDo>: 차원축소된 벡터공간에서의 분산 유지율을 계산합니다.
    order = (-model.lambda_).argsort()
    shrinked_var = model.lambda_[order].sum()
    
    # <ToDo>: 차원축소된 벡터공간에서 유지된 분산을 원본의 분산으로 나눠 분산 유지율을 계산해 반환합니다.
    return shrinked_var / original_var

# <TODO> 여러분이 답으로 제출하고 싶은 군집의 개수로 your_choice 함수의 '?' 부분에 넣은 후 제출하세요.
def your_choice(X):
    myPCA = md.PCA(n_components = 5)
    myPCA.fit_transform(X)
    
    return myPCA


def main():

    X = pre.load_data()
    
    # <TODO> PCA의 n_components에 성분의 개수를 입력해 여러가지 PCA 모델을 시도해보세요.
    myPCA = your_choice(X)
    
    # <ToDo>: 모델 학습의 결과로 원본 대비 축소후의 분산의 비율을 계산합니다.
    percentage = variance_calculator(myPCA, X)
    
    # 축소후 차원의 수와 원본 대비 축소후의 분산의 비율을 출력합니다. 
    print('원본 데이터의 차원 = {}, n_components = {}, 원본 대비 축소후의 분산의 비율: {}'.format(X.shape[1], 2, percentage))
    

if __name__ == "__main__":
    main()