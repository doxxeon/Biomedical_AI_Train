'''
Q1. 문자열을 반대로 뒤집는 함수 작성하기

주어진 문자열을 반대로 뒤집는 함수 reverse_string을 작성하세요. 
예를 들어, 입력 문자열이 “Python”이면 출력은 “nohtyP”이어야 합니다.
'''

def reverse_string(str):
    return str[::-1] 
    # 처음부터 -1 간격으로 출력
    # 문법이니 외우고 있기
    # "::" 을 기준으로 왼쪽 이상부터 오른쪽 간격으로 출력

str = 'Python'
reverse_string(str)