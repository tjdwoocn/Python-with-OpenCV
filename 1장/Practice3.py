# OpenCV 창에서 버튼 및 탐색바와 같은 UI 요소로 작업
import argparse
import cv2
import numpy as np

cv2.namedWindow('window')

# 색상 구성 요소 추가
fill_val = np.array([255,255,255], np.uint8)

# 각 trackbar_callback 함수에서 호출하는 보조 함수를 추가
# 이 함수는 색상 구성 요소 인덱스와 설정될 새 값을 받는다
def trackbar_callback(idx, value):
    fill_val[idx] = value

# 세 개의 탐색 바를 window에 추가하고 파이썬 lambda 함수를 사용해
# 각 탐색바 콜백을 특정 색상 구성 요소에 바인딩한다
cv2.createTrackbar('R', 'window', 255, 255,
                  lambda v: trackbar_callback(2,v))
cv2.createTrackbar('G', 'window', 255, 255,
                  lambda v: trackbar_callback(1,v))
cv2.createTrackbar('B', 'window', 255, 255,
                  lambda v: trackbar_callback(0,v))

while True:
    image = np.full((500,500,3), fill_val)
    cv2.imshow('window', image)
    key = cv2.waitKey(3)
    if key ==27:
        break

cv2.destroyAllWindows()

