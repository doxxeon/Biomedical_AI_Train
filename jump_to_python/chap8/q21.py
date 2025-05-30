import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "<html><head><Title>제목</head></html>"

p1 = "<.*>"          #<html>부터 </html>까지 모두 출력
p2 = "<.*?>"         #정규표현식을 이용해보세요.

m1 = re.findall(p1, text)
m2 = re.findall(p2, text)

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)
