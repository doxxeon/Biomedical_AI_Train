'''
Q9. 다음과 같이 실행할 때 입력값을 모두 더해서 출력하는 스크립트(C:\doit\myargv.py)를 작성해보자.

>>> C:\cd doit
>>> C:\doit> python myargv.py 1 2 3 4 5 6 7 8 9 10
55
'''

# myargv.py
import sys

numbers = sys.argv[1:]

result = 0
for i in numbers:
    result += int(i)  

print(result)


