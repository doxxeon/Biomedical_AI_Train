import pandas as pd

def load_data(path, independent_var, response_var):
    
    data = pd.read_csv(path, header=0)
    
    data = data[(data['class_num'] == 1) | (data['class_num'] == 2)]
    
    x_mat = data.loc[:, independent_var].values.reshape(-1, 2)
    y_vec = data.loc[:, response_var].values.reshape(-1, )
    
    # 전체 데이터를 훈련용과 검증용으로 나눕니다.
    x_train = x_mat[10:]
    y_train = y_vec[10:]
    x_val = x_mat[0:10]
    y_val = y_vec[0:10]
    
    return x_train, y_train, x_val, y_val