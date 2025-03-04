'''
문제 2

아래와 같은 클래스 BankAccount을 생성하세요:

클래스 속성: account_number, balance
생성자: __init__(self, account_number, balance=0): account_number와 초기 잔액 balance(기본값 0)을 인자로 받아 객체를 초기화합니다.
메소드: deposit(self, amount): 계좌에 amount만큼 입금합니다.
메소드: withdraw(self, amount): 계좌에서 amount만큼 출금합니다. 잔액이 출금액보다 작을 경우 “잔액이 부족합니다”라고 출력합니다.
예시 코드를 작성하고 테스트해보세요.

class BankAccount:
    # 여기에 코드를 작성하세요

account1 = BankAccount(12345, 1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)  # 출력: 잔액이 부족합니다
'''

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다.")
        else:
            self.balance -= amount


account1 = BankAccount(12345, 1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)  # 출력: 잔액이 부족합니다
