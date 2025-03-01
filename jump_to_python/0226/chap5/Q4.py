'''
Q4. filter와 lambda를 사용해서 리스트 [1,-2,3,-5,8,-3]에서 음수를 제거해보자.
'''

print(list(filter(lambda x: x>0, [1, -2, 3, -5, 8, -3])))
# filter(f, iterable)은 iterable에서 f함수를 통과한 요소만을 구성하는 iterator를 반환한다.

