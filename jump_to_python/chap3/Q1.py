'''
Q1. 홍길동의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수는?

국어 - 80, 영어 -75, 수학 - 55
'''

hong = {'국어': 80,
        '영어': 75,
        '수학': 55}
a, b, c = hong.values()
score = a+b+c
print(float(score/3))

#또는

kor = 80
eng = 75
math = 55
sum = kor + eng + math
print(sum/3)