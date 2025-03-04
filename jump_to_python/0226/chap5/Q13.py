'''
Q13. random 모듈을 이용해서 로또번호(1~45사이의 숫자 6개)를 생성해보자. (중복 숫자 안 됨)
'''

import random

'''
lotto = random.sample(range(1, 46),6)
'''

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)
