'''
문제 8

아래 코드는 두 숫자를 나누는 코드입니다. 분모가 0인 경우, ZeroDivisionError 예외가 발생할 수 있습니다. 이 예외를 처리하고, 사용자에게 0으로 나눌 수 없다는 메시지를 출력하는 코드를 작성하세요.

numerator = 10
denominator = 0
result = numerator / denominator
print("결과:", result)
'''

numerator = 10
denominator = 0

try:
    result = numerator / denominator
    print("결과:", result)

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

finally:
    print("프로그램을 종료합니다.")

