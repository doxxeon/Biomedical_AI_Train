'''
소수를 판별하는 함수 작성하기

주어진 숫자가 소수인지 아닌지를 판별하는 함수 is_prime을 작성하세요. 소수는 1과 자기 자신만을 약수로 갖는 1보다 큰 양의 정수입니다. 함수는 소수일 경우 True를 반환하고, 아닐 경우 False를 반환해야 합니다.

'''

def is_prime(num):
    for i in range (num):
        if num%i==0:
            print("False")
        i+=1
    print("True")

num = int(input("숫자 입력: "))
is_prime(num)