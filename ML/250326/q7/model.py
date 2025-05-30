import numpy as np
from scipy.linalg import svd

class PCA:
    def __init__(self, n_components ):
        self.n_components = n_components # 군집의 개수
        self.lambda_ = [0 , 0] #학습시, 고유값을 저장합니다.
        self.V =  np.empty([2,2])# 학습시, 고유 벡터를 저장합니다.
        self.mean_ = np.empty([1,2]) # 학습시, 데이터 포인트의 평균을 저장합니다.
        self.W = np.empty([1,2]) # 학습시, 변환 행렬을 저장합니다.
    
    def fit_transform(self, X):
        
        self.mean_ = X.mean(axis = 0)
        
        diff = X - self.mean_
        cov = diff.T.dot(diff)
        
        self.V, self.lambda_, _ = svd(cov)
        
        order = (-self.lambda_).argsort()
        self.W = self.V[:,order[0:self.n_components]]
        
        return (X - self.mean_).dot(self.W)

    def inverse_transform(self, X_hat):
        
        return (X_hat).dot(self.W.T) + self.mean_
