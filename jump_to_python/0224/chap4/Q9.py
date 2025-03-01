'''
Q9. 다음과 같은 딕셔너리 a가 있다. 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.

1. a[‘name’] = ‘python’
>> 새로운 key: 'name', value: 'python'

2. a[(‘a’,)] = ‘python’
>> 새로운 key: 'a',, value: 'python'

3. a[[1]] = ‘python’

4. a[250] = ‘python’
>> 새로운 key: 250, value: 'python'
'''

# 3번이 오류이다.
# 딕셔너리의 key로 list가 올 수 없는 이유는 list가 가변 데이터로 이루어져있기 때문이다.