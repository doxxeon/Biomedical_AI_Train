'''
문제 7

아래 코드는 사용자로부터 숫자를 입력받아 제곱을 출력하는 코드입니다. 사용자가 숫자가 아닌 문자를 입력할 경우, ValueError 예외가 발생할 수 있습니다. 이 예외를 처리하고, 사용자에게 숫자를 입력하도록 안내하는 코드를 작성하세요.

number = input("숫자를 입력하세요: ")
squared_number = int(number) ** 2
print("입력한 숫자의 제곱:", squared_number)
'''


try:
    number = input("숫자를 입력하세요: ")
    squared_number = int(number) ** 2
    print("입력한 숫자의 제곱:", squared_number)
except ValueError:
    print("숫자를 입력해야 합니다.")
finally:
    print("프로그램을 종료합니다.")

