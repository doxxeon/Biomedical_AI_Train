import numpy as np
import matplotlib.pyplot as plt

'''
1. AND_gate 함수를 완성하세요.

   Step01. 입력값 x1과 x2에 각각 곱해줄 가중치는
           0.5, 0.5로 설정되어 있습니다.
           
   Step02. AND_gate를 만족하는 Bias 값을
           설정합니다. 여러 가지 값을 대입해보며
           적절한 Bias 값을 찾아보세요.
   
   Step03. 가중치, 입력값, Bias를 이용하여 
           신호의 총합을 구합니다.
           
   Step04. Step Function 함수를 호출하여 
           AND_gate의 출력값을 반환합니다.
'''

def AND_gate(x1, x2):
    
    x = np.array([x1, x2])
    
    weight = np.array([0.5,0.5])
    
    bias = -0.6
    
    if x[0] * weight[0] + x[1] * weight[1] + bias >= 0:
        y = 1
    else:
        y = 0
    
    return Step_Function(y)
    
'''
2. OR_gate 함수를 완성하세요.

   Step01. 입력값 x1과 x2에 각각 곱해줄 가중치는
           0.5, 0.5로 설정되어 있습니다.
           
   Step02. OR_gate를 만족하는 Bias 값을
           설정합니다. 여러 가지 값을 대입해보며
           적절한 Bias 값을 찾아보세요.
   
   Step03. 가중치, 입력값, Bias를 이용하여 
           신호의 총합을 구합니다.
           
   Step04. Step Function 함수를 호출하여 
           OR_gate의 출력값을 반환합니다.
'''

def OR_gate(x1, x2):
        x = np.array([x1, x2])
    
        weight = np.array([0.5,0.5])
    
        bias = -0.1

        if x[0] * weight[0] + x[1] * weight[1] + bias >= 0:
                y = 1
        else:
                y = 0
    
    
        return Step_Function(y)

'''
3. 설명을 보고 Step Function을 완성합니다.

   Step01. 0 미만의 값이 들어오면 0을,
           0 이상의 값이 들어오면 1을
           출력하는 함수를 구현하면 됩니다.
'''
def Step_Function(y):
        if y >= 0:
                return 1
        else:
                return 0
    
def main():
    
    # AND Gate와 OR Gate에 넣어줄 Input
    array = np.array([[0,0], [0,1], [1,0], [1,1]])
    
    # AND Gate를 만족하는지 출력하여 확인
    print('AND Gate 출력')
    
    for x1, x2 in array:
        print('Input: ',x1, x2, ', Output: ',AND_gate(x1, x2))
    
    # OR Gate를 만족하는지 출력하여 확인
    print('\nOR Gate 출력')
    
    for x1, x2 in array:
        print('Input: ',x1, x2, ', Output: ',OR_gate(x1, x2))

if __name__ == "__main__":
    main()
