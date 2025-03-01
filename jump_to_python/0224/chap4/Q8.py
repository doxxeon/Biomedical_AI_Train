'''
Q8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
'''

tuple1 = (1,2,3)
list_new = list(tuple1)
list_new.append(4)
tuple1=tuple(list_new)
print(tuple1)
