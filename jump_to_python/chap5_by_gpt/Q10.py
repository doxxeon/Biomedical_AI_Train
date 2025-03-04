'''
문제 10

주어진 문자열에서 공백을 기준으로 단어를 분리하고, 
각 단어의 첫 글자를 대문자로 변경한 후, 
다시 공백을 기준으로 합쳐서 출력하는 코드를 작성하세요. 
이 문제를 해결하기 위해 str.split(), str.capitalize(), 
str.join() 내장 함수를 사용하세요.
'''

text = "hello world, this is a python example."
words = text.split()

''' # 이 부분을 한 줄로 간단하게 줄일 수 있다 !! (리스트 컴프리핸션)
capitalized_words = []
for word in words:
    capitalized_word = word.capitalize() 
    capitalized_words.append(capitalized_word)
result = " ".join(capitalized_words)
'''

capitalized_words = [words.capitalize() for word in words]

result = " ".join(capitalized_words)

print(result)

