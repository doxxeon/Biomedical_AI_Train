'''
문제 11

파이썬 datetime 모듈을 사용하여 현재 시간을 출력하는 코드를 작성하세요.
'''

from datetime import datetime

current_time = datetime.now()
# type(current_time) -> <class 'datetime.datetime'> // datetime 객체
print(current_time)

