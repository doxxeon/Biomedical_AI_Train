'''
Q3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해보자.

  *
  **
  ***
  ****
  *****

'''

i = 0
while True:
  i += 1
  if i>5:
    break
  print('*' * i)
