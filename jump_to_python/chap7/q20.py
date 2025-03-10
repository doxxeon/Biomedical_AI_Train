'''
20. 전방 탐색
다음은 이메일 주소를 나타내는 정규식이다. 
이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr 등과 매치된다.
긍정형 전방 탐색 기법을 사용하여 .com, .net이 아닌 이메일 주소는 제외시키는 정규식을 작성하시오.

.*[@].*[.].*$
'''

import re

text = '''
park@naver.com
kim@daum.net
lee@myhome.co.kr
'''

p = re.compile(".+@.+(?=\.(com|net)$)")

m = p.findall(text)

print(m)

# 또는

pattern = r"."[@]."[.](?=com$|net$)."$"