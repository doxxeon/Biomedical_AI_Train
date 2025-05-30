'''
Q1. 아래와 같은 클래스 Person을 생성하세요

클래스 속성: name, age
생성자: __init__(self, name, age): name과 age를 인자로 받아 객체를 초기화합니다.
메소드: greet(self): "{name}님이 {age}살입니다" 형식의 문자열을 반환합니다.
예시 코드를 작성하고 테스트해보세요.

class Person:
    # 여기에 코드를 작성하세요

person1 = Person("홍길동", 30)
print(person1.greet())  # 출력: 홍길동님이 30살입니다
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'{self.name}님이 {self.age}살입니다.')

person1 = Person("홍길동", 30)
print(person1.greet())

