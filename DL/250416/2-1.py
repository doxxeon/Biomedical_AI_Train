import numpy as np

# 사용할 1차 선형 회귀 모델

def linear_model(w0, w1, X):
    
    f_x = w0 + w1 * X
    
    return f_x
    
'''
1. 설명 중 '손실 함수' 파트의 수식을 참고해
   MSE 손실 함수를 완성하세요. 
'''

def Loss(f_x, y):
    
    ls = np.mean((f_x - y) ** 2)
    
    return ls

'''
2. 설명 중 'Gradient' 파트의 마지막 두 수식을 참고해 두 가중치
   w0와 w1에 대한 gradient인 'gradient0'와 'gradient1'을
   반환하는 함수 gradient_descent 함수를 완성하세요.
   
   Step01. w0에 대한 gradient인 'gradient0'를 작성합니다.
   
   Step02. w1에 대한 gradient인 'gradient1'을 작성합니다.
'''

def gradient_descent(w0, w1, X, y):
    
    gradient0 = (-2/X.size) * np.sum(y - (w0 + w1 * X))
    gradient1 = (-2/X.size) * np.sum((y - (w0 + w1 * X)) * X)
    
    return np.array([gradient0, gradient1])

'''
3. 설명 중 '가중치 업데이트' 파트의 두 수식을 참고해 
   gradient descent를 통한 가중치 업데이트 코드를 작성하세요.
   
   Step01. 앞서 완성한 gradient_descent 함수를 이용해
           w0와 w1에 대한 gradient인 'gd'를 정의하세요.
           
   Step02. 변수 'w0'와 'w1'에 두 가중치 w0와 w1을 
           업데이트하는 코드를 작성합니다. 앞서 정의한
           변수 'gd'와 이미 정의된 변수 'lr'을 사용하세요.
'''

def main():
    
    X = np.array([1,2,3,4]).reshape((-1,1))
    y = np.array([3.1, 4.9, 7.2, 8.9]).reshape((-1,1))
    
    # 파라미터 초기화
    w0 = 0
    w1 = 0
    
    # learning rate 설정
    lr = 0.001
    
    # 반복 횟수 1000으로 설정
    for i in range(1000):
    
        gd = gradient_descent(w0, w1, X, y)
        w0 = w0 - lr * gd[0]
        w1 = w1 - lr * gd[1]
        
        # 100회마다의 해당 loss와 w0, w1 출력
        if (i % 100 == 0):
        
            loss = Loss(linear_model(w0,w1,X),y)
        
            print("{}번째 loss : {}".format(i, loss))
            print("{}번째 w0, w1 : {}, {}".format(i, w0, w1),'\n')

    return w0, w1

if __name__ == '__main__':
    main()
