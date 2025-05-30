import numpy as np

'''
1. XOR_gate 함수를 최대한 완성해보세요.

   Step01. 이전 실습을 참고하여 입력값 x1과 x2를
           Numpy array 형식으로 정의한 후, x1과 x2에
           각각 곱해줄 가중치도 Numpy array 형식으로 
           적절히 설정해주세요.
           
   Step02. XOR_gate를 만족하는 Bias 값을
           적절히 설정해주세요.
           
   Step03. 가중치, 입력값, Bias를 이용하여 
           가중 신호의 총합을 구합니다.
           
   Step04. Step Function 함수를 호출하여 
           XOR_gate 출력값을 반환합니다.
'''

def XOR_gate(x1, x2):
    
    x = np.array([x1, x2])
    
    weight = np.array([0.5, 0.5])
    
    bias = -0.3
    
    if x[0] * weight[0] + x[1] * weight[1] + bias >= 0:
        y = 1
    else:
        y = 0
    
    return Step_Function(y)

'''
2. 설명을 보고 Step Function을 완성합니다.
   앞 실습에서 구현한 함수를 그대로 
   사용할 수 있습니다.

   Step01. 0 미만의 값이 들어오면 0을,
           0 이상의 값이 들어오면 1을
           출력하는 함수를 구현하면 됩니다.
'''

def Step_Function(y):
    if y >=0:
        return 1
    else:
        return 0

def main():
    
    # XOR Gate에 넣어줄 Input과 그에 따른 Output
    Input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])        
    Output = np.array([[0], [1], [1], [0]])
    
    # XOR Gate를 만족하는지 출력하여 확인
    print('XOR Gate 출력')
    
    XOR_list = []
    
    for x1, x2 in Input:
        print('Input: ',x1, x2, ' Output: ', XOR_gate(x1, x2))
        XOR_list.append(XOR_gate(x1, x2))
    
    hit = 0
    for i in range(len(Output)):
        if XOR_list[i] == Output[i]:
            hit += 1
    
    acc = float(hit/4)*100
    
    print('Accuracy: %.1lf%%' % (acc))

if __name__ == "__main__":
    main()
