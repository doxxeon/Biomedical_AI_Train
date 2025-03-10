'''
Q2. while문을 사용해 1부터 1000까지 자연수 중 3의 배수의 합을 구하라.
'''

result = 0

i = 1
while i <= 1000:
    if (i%3 == 0):
     result += i
    i += 1

print(result)