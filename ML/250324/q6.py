import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

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

	return X,y,feature_names

    
"""
2. 릿지(Ridge) 회귀를 구현하고, 
   전체 데이터를 바탕으로 학습시킨 모델을 
   반환하는 함수를 완성합니다.
"""
def Ridge_regression(X, y):
    
    ridge_reg = Ridge(alpha=10)
    
    ridge_reg.fit(X, y)
    
    return ridge_reg

"""
3. 라쏘(Lasso) 회귀를 구현하고, 
   전체 데이터를 바탕으로 학습시킨 모델을 
   반환하는 함수를 완성합니다.
"""
def Lasso_regression(X, y):
    
    lasso_reg = Lasso(alpha=10)
    
    lasso_reg.fit(X,y)
    
    return lasso_reg
    
# 각 변수의 beta_i 크기를 시각화하는 함수입니다.
def plot_graph(coef, title):
    fig = plt.figure()
    
    plt.ylim(-1,1)
    plt.title(title)
    coef.plot(kind='bar')

    plt.savefig(f"{title}result.png")


def main():
    
    X,y,feature_names = load_data()
    
    ridge_reg = Ridge_regression(X, y)
    lasso_reg = Lasso_regression(X, y)
    
    ## Ridge 회귀의 beta_i의 크기를 저장합니다.
    ridge_coef = pd.Series(ridge_reg.coef_, feature_names).sort_values()
    print("Ridge 회귀의 beta_i\n", ridge_coef)
    
    ## Lasso 회귀의 beta_i의 크기를 저장합니다.
    lasso_coef = pd.Series(lasso_reg.coef_, feature_names).sort_values()
    print("Lasso 회귀의 beta_i\n", lasso_coef)
    
    plot_graph(ridge_coef, 'Ridge')
    plot_graph(lasso_coef, 'Lasso')

if __name__=="__main__":
    main()
