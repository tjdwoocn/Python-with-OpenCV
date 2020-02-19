# 프레임 스트림 property 얻기
# 프레임 높이와 너비, 비디오 파일의 프레임 수 및
# 카메라 프레임 속도와 같은 VideoCapture 프로퍼티를 얻는 방법

import numpy as np
import cv2

def print_capture_properties(*args):
    capture = cv2.VideoCapture(*args)
    print('Created capture: ', ' '.join(map(str, args)))
    print('Frame count:', int(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
    print('Frame width: ', int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height: ', int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('Frame rate: ', capture.get(cv2.CAP_PROP_FPS))

path = ('./data/drop.avi')
print_capture_properties(path)
print_capture_properties(0)

# 프로퍼티 ID를 받아 그 값을 부동소수점 값으로 반환하는 capture.get
# 함수를 사용해 프로퍼티를 가져온다
