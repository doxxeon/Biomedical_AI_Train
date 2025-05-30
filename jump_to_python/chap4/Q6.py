'''
Q6. 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해보자.
(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야한다.)
'''

user_input = input("저장할 내용을 입력하세요 : ")
f = open('test.txt', 'a', encoding='utf-8')
f.write(user_input)
f.write('\n')
f.close()
