'''
1. 신호의 총합과 외출 여부를 반환하는 
   Perceptron 함수를 완성합니다.

   Step01. Bias는 외출을 좋아하는 정도이며1
           -1로 설정되어 있습니다.
   
   Step02. 입력 받은 값과 Bias 값을 이용하여 신호의
           총합을 구합니다.
           ddd
   Step03. 지시한 활성화 함수를 참고하여 외출 여부
           (0 or 1)를 반환합니다.
'''

def Perceptron(x_1,x_2,w_1,w_2):
    
    bias = -1
    
    output = x_1 * w_1 + x_2 * w_2 + bias
    
    if output > 0:
        y = 1
    else:
        y = 0
    
    return output, y

# 값을 입력받는 함수입니다.

def input_func():
    
    # 비 오는 여부(비가 온다 : 1 / 비가 오지 않는다 : 0)
    x_1 =  int(input("x_1 : 비가 오는 여부(1 or 0)을 입력하세요."))
    
    # 여자친구가 만나자고 하는 여부(만나자고 한다 : 1 / 만나자고 하지 않는다 : 0)
    x_2 =  int(input("x_2 : 여친이 만나자고 하는 여부(1 or 0)을 입력하세요."))
    
    # 비를 좋아하는 정도의 값(비를 싫어한다 -5 ~ 5 비를 좋아한다)
    w_1 =  int(input("w_1 : 비를 좋아하는 정도 값(-5 ~ 5)을 입력하세요."))
    
    # 여자친구를 좋아하는 정도의 값(여자친구를 싫어한다 -5 ~ 5 비를 좋아한다)
    w_2 =  int(input("w_2 : 여친을 좋아하는 정도 값(-5 ~ 5)을 입력하세요."))
    
    return x_1, x_2, w_1, w_2
    
'''
2. 실행 버튼을 눌러 x1, x2, w1, w2 값을 다양하게
   입력해보고, Perceptron함수에서 반환한 신호의 총합과
   그에 따른 외출 여부를 확인해보세요
'''
    
def main():
    
    x_1, x_2, w_1, w_2 = input_func()
    
    result, go_out = Perceptron(x_1,x_2,w_1,w_2)
    
    print("\n신호의 총합 : %d" % result)
    
    if go_out > 0:
        print("외출 여부 : %d\n ==> 외출한다!" % go_out)
    else:
        print("외출 여부 : %d\n ==> 외출하지 않는다!" % go_out)
    
if __name__ == "__main__":
    main()