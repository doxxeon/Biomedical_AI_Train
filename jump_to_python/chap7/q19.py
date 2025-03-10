'''
다음과 같은 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식을 사용하여 작성하시오.

"""
park 010-9999-9998
kim 010-9909-7789
lee 010-8789-7768
"""
'''

import re

text = '''
park 010-9999-9998
kim 010-9909-7789
lee 010-8789-7768
'''

pattern = re.compile("(010)\D?\d{4}\D?(\d{4})")
print("결과: ", re.sub(pattern, "\g<1>-####-\g<2>", text))

# 또는

modified_text = re.sub(r'(\d{3}-\d{4}-)\d{4}', r'\1####', text)
print(modified_text)
