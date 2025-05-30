'''
문제 4

파이썬 표준 라이브러리 random 모듈을 사용하여 1부터 100 사이의 무작위 정수를 10개 생성하고, 이를 오름차순으로 정렬하는 코드를 작성하세요.

예시 코드를 작성하고 테스트해보세요.
'''

import random

random_numbers = [random.randint(1, 100) for _ in range(10)]
random_numbers.sort()
print(random_numbers)
