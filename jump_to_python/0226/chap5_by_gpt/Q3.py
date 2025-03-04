'''
문제 3

아래와 같은 간단한 모듈 calculator.py를 작성하고, 다른 파이썬 스크립트에서 이 모듈을 사용해보세요.

함수: add(a, b): 두 숫자의 합을 반환합니다.
함수: subtract(a, b): 두 숫자의 차를 반환합니다.
함수: multiply(a, b): 두 숫자의 곱을 반환합니다.
함수: divide(a, b): 두 숫자의 나눗셈 결과를 반환합니다. 0으로 나누는 경우, “0으로 나눌 수 없습니다”라고 출력합니다.
예시 코드를 작성하고 테스트해보세요.

# calculator.py 파일
# 여기에 코드를 작성하세요

# main.py 파일
import calculator

print(calculator.add(3, 4))      # 출력: 7
print(calculator.subtract(3, 4)) # 출력: -1
'''

# calculator.py 파일
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        print("0으로 나눌 수 없습니다.")    
    else:
        return a/b
    
# main.py 파일
import calculator

print(calculator.add(3, 4))      # 출력: 7
print(calculator.subtract(3, 4)) # 출력: -1
