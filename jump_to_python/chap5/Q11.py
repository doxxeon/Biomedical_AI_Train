'''
Q11. glob모듈을 사용해서 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 만들어보자.
'''

import glob

print(glob.glob("c:\\doit\\*.py")) # glob.glob()은 해당 디렉터리에 있는 파일들을 리스트로 만들어서 반환한다.

