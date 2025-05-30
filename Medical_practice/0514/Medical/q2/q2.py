import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def create_histogram(images, channels, mask, histSize, ranges):
    histr = cv.calcHist(images, channels, mask, histSize, ranges)
    return histr


def create_mask(img, x_range, y_range):
    mask = np.zeros(img.shape[:2], np.uint8)
    # x축의 x1~x2 구간, y축의 y1~y2 구간에 255의 값을 할당합니다.
    mask[y_range[0] : y_range[1], x_range[0] : x_range[1]] = 255
    
    # cv.bitwise_and()함수를 활용하여 masked_img를 구현합니다.
    masked_img = cv.bitwise_and(img, img, mask=mask)
    return mask, masked_img


def main():
    img = cv.imread("normal.PNG", cv.IMREAD_GRAYSCALE)
    height, width = img.shape

    """
    지시사항 1. channels 에 적절한 값을 입력하세요.
    실습에서 사용하는 이미지는 gray scale 입니다.
    """
    channels = None
    
    # 전체 영역에 대한 계산을 수행합니다. (수정 부분 X)
    mask = None
    # 히스토그램의 bin 갯수
    histSize = [256]
    
    """
    지시사항 2. 모든 그레이 레벨(명암)을 사용하도록 ranges 범위를 조정하세요. 
    """
    ranges = [None, None]

    # 원래 이미지의 히스토그램을 출력합니다.
    hist_full = create_histogram([img], channels, mask, histSize, ranges)

    """
    지시사항 3. 이미지에 마스킹을 할 부분을 지정하기 위해
    x_range와 y_range의 범위를 지정하세요.
    이미지의 가로와 세로 크기인 width, height를 활용하세요.
    """
    x_range = [None, None]
    y_range = [None, None]
    
    mask, masked_img = create_mask(img, x_range, y_range)
    
    # 마스크를 포함한 히스토그램과 제외한 히스토그램을 출력합니다.
    hist_mask = create_histogram([img], channels, mask, histSize, ranges)

    plt.subplot(221), plt.imshow(img, "gray")
    plt.subplot(222), plt.imshow(masked_img, "gray")
    plt.subplot(223), plt.plot(hist_full)
    plt.xlim([0, 256])
    plt.subplot(224), plt.plot(hist_mask)
    plt.xlim([0, 256])
    plt.show()

    # 엘리스 화면에 그래프를 표시합니다.
    plt.savefig("masked_graph.png")
    plt.close()

    return channels, ranges, x_range, y_range


if __name__ == "__main__":
    main()
