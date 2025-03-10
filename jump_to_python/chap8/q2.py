
import re

text = "abcdefg"

pattern = re.compile("e")

print("정규식 객체의 자료형 : ", type(pattern))

print("정규식 객체 사용하는 경우 : ", pattern.findall(text))

print("객체를 사용하지 않는 경우 : ", re.findall("e", text))  
# 위 코드와 동일한 코드이기 때문에, 정의한 정규표현식을 여러 번 사용할 때 주로 이용