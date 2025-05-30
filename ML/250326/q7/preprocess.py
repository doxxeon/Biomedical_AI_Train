import numpy as np
import csv

def load_data():
    
    f = open('ML/250326/q7/iris.csv', 'r', encoding='utf-8')
    raw_data = csv.reader(f)
    
    # 붓꽃 데이터를 한 줄씩 읽어와 float 형으로 빈 리스트 sepal_length, sepal_width, petal_length, petal_width에 저장합니다.
    # 데이터의 이름 표지 'sepal_length', 'sepal_width', `petal_length`, `petal_width`는 list에 포함하지 않습니다.
    
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    
    for lines in raw_data:
        sepal_length.append(lines[0])
        sepal_width.append(lines[1])
        petal_length.append(lines[2])
        petal_width.append(lines[3])
    
    # 생성된 sepal_length, sepal_width 리스트를 각각 float 형 numpy array로 변환하고, 최종적으로 두 열벡터를 합쳐 열이 2개인 ndarray를 출력합니다.
    sepal_length = np.array(sepal_length[1:]).astype(np.float64)
    sepal_width = np.array(sepal_width[1:]).astype(np.float64)
    petal_length = np.array(petal_length[1:]).astype(np.float64)
    petal_width = np.array(petal_width[1:]).astype(np.float64)
        
    return np.stack((sepal_length, sepal_width, petal_length, petal_width), axis = 1)