'''
문제 6

위의 my_math 패키지에 다음과 같이 새로운 모듈 geometry.py를 추가하세요.

모듈: geometry.py
함수: circle_area(radius): 원의 반지름을 입력받아 넓이를 반환합니다. (넓이 = 반지름 x 반지름 x π)
함수: rectangle_area(width, height): 사각형의 가로와 세로를 입력받아 넓이를 반환합니다. (넓이 = 가로 x 세로)
패키지를 수정한 후, 다른 파이썬 스크립트에서 이 패키지를 사용해보세요.

예시 코드를 작성하고 테스트해보세요
'''

# my_math/geometry.py 파일 생성
# geometry.py 파일
import math

def circle_area(radius):
    return radius*radius*math.pi

def rectangle_area(width, height):
    return width*height

# main.py 파일

from my_math.geometry import circle_area, rectangle_area

print(circle_area(5))
print(rectangle_area(4,5))
