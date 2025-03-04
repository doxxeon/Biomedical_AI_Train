'''
문제 5

아래와 같은 간단한 패키지 my_math를 생성하세요.

패키지: my_math
모듈: operations.py
함수: add(a, b): 두 숫자의 합을 반환합니다.
함수: subtract(a, b): 두 숫자의 차를 반환합니다.
패키지를 생성한 후, 다른 파이썬 스크립트에서 이 패키지를 사용해보세요.

예시 코드를 작성하고 테스트해보세요.
'''

# my_math 패키지 생성
# my_math/operations.py 파일 생성
# operations.py 파일
def add(a, b):
    return a+b  

def subtract(a, b):
    return a-b

# main.py 파일
from my_math.operations import add, subtract

print(op.add(3, 4))      # 출력: 7
print(op.subtract(3, 4)) # 출력: -1
