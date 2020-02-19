# 카메라 프레임 캡처 및 표시
# OpenCV 를 사용해 USB 카메라에 연결해 실시간으로 프레임을 캡처 하는 방법이다

import argparse
import cv2
import numpy as np

# VideoCapture 객체 생성
capture = cv2.VideoCapture(0)

# 읽기 성공 플래그와 frame으로 된 페어를 반환하는
# capture.read 함수를 사용해 카메라에서 프레임을 읽는다
while True:
    has_frame, frame = capture.read()
    if not has_frame:
        print('Can\'t get frame')

    cv2.imshow('frame', frame)
    key = cv2.waitKey(3)
    if key == 27:
        print('Pressed Esc')
        break

capture.release()
cv2.destroyAllWindows()

# OpenCV의 카메라 동작은 cv2.VideoCapture 클래스를 통해 수행됨
# 사실 해당 클래스는 카메라와 비디오 파일의 동작을 모두 지원
# 카메라의 프레임 스트림을 나타내는 객체의 인스턴스화는
# 0부터 시작하는 장치의 인덱스 번호를 지정하면 됨
# OpenCV에서 기본적으로 지원하지 않는 카메라를 사용한다면
# OpenCV를 다른 산업용 카메라 유형을 지원하는 옵션을 켜고 다시 컴파일해야함
