import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# boston 데이터를 위한 모듈을 불러옵니다. 
#from sklearn.datasets import load_boston

"""
1. 사이킷런에 존재하는 데이터를 불러오고, 
   불러온 데이터를 학습용 데이터와 테스트용 데이터로
   분리하여 반환하는 함수를 구현합니다.
"""
def load_data():  
    data_url="http://lib.stat.cmu.edu/datasets/boston"  
    raw_df=pd.read_csv(data_url,sep="\s+",skiprows=22,header=None)  
    X=np.hstack([raw_df.values[::2,:],raw_df.values[1::2,:2]])  
    y=raw_df.values[1::2,2]  
	#X, y = load_boston(return_X_y = True)  
    feature_names=np.array(['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD', 'TAX','PTRATIO','B','LSTAT'], dtype='<U7')
    print("데이터의 입력값(X)의 개수 :", X.shape[1])
    train_X, test_X, train_y, test_y = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=100)
    
    return train_X, test_X, train_y, test_y
	#return X,y,feature_names

    
"""
2. 다중 선형회귀 모델을 불러오고, 
   불러온 모델을 학습용 데이터에 맞추어 학습시킨 후
   해당 모델을 반환하는 함수를 구현합니다.

"""
def Multi_Regression(train_X,train_y):
    
    multilinear = LinearRegression()
    
    multilinear.fit(train_X, train_y)
    
    return multilinear
    
"""
3. 모델 학습 및 예측 결과 확인을 위한 main 함수를 완성합니다.
"""
def main():
    
    train_X, test_X, train_y, test_y = load_data()
    
    multilinear = Multi_Regression(train_X,train_y)
    
    predicted = multilinear.predict(test_X)
    
    model_score = multilinear.score(test_X, test_y)
    
    print("\n> 모델 평가 점수 :", model_score)
     
    beta_0 = multilinear.intercept_
    beta_i_list = multilinear.coef_
    
    print("\n> beta_0 : ",beta_0)
    print("> beta_i_list : ",beta_i_list)
    
    return predicted, beta_0, beta_i_list, model_score
    
if __name__ == "__main__":
    main()
