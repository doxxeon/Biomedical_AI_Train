'''
Q12. time모듈을 사용해서 현재 날짜와 시간을 다음과 같은 형식으로 출력해보자.
2018/04/03 17:20:32
'''

import time

print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())))
