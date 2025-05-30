'''
Q10. os모듈을 사용해서 다음과 같이 동작하도록 코드를 작성해라.

C:\doit 디렉터리로 이동한다.
dir 명령을 실행하고 그 결과를 변수에 담는다.
dir 명령의 결과를 출력한다.
'''

import os

os.chdir("c:\\doit")
result = os.popen("dir")
print(result.read())
result.close()


