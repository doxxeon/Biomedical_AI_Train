'''
Q3. 홍길동의 주민등록번호는 881120-1068234이다. 홍길동의 주민등록번호를 연원일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.
'''

hongs = [8,8,1,1,2,0,1,0,6,8,2,3,4]
birth = hongs.copy()
del birth [6:]
others = hongs.copy()
del others [:6]
print("연월일: ",birth,", 뒷자리: ",others)

#또는

num = '881120-1068234'
print(num[:6])
print(num[7:])

print(num.split('-'))