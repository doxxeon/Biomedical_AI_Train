'''
18. 문자열 검색 다음 코드의 결과값은 무엇일까?

import re p = re.compile("[a-z]+") m = p.search("5 python") print(m.start() + m.end())
'''

import re 


p = re.compile("[a-z]+") 
m = p.search("5 python") 

print(m.start() + m.end()) # 인덱스 2 + 인덱스 8 = 10

# 예상 출력: python
# 실제 출력: 10