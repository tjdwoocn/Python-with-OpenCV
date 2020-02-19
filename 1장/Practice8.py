# 비디오 프레임 스트림 재생
# OpenCV를 통해 기존 비디오 파일을 여는 방법
# 열린 비디오의 프레임을 다시 재생하는 방법

import cv2

# VideoCapture 객체 생성
capture = cv2.VideoCapture('./data/drop.avi')

# 비디오의 모든 프레임을 다시 재생한다
while True:
    has_frame, frame = capture.read()
    if not has_frame:
        print('Reached the end of the video')
        break

    cv2.imshow('frame', frame)
    key = cv2.waitKey(50)  # 함수 안의 숫자만큼 기다렸다가 다음 프레임을 보여준다
    if key == 27:  # ESC 키의 코드가 27임
        print('Pressed ESC')
        break

cv2.destroyAllWindows()

# 비디오 파일로 작업하는 것은 카메라로 작업하는 것과 사실상 동일
# 동일한 cv2.VideoCapture 클래스를 통해 수행
# while 루프에서 비디오 파일을 연 후에는 capture.read 함수를 사용해 프레임을 가져온다
# 이 함수는 프레임 읽기 성공 여부에 대한 불리언 값과 프레임으로 구성된 페어를 반환한다
# 프레임은 가능한 한 빠른 속도로 읽어오기 때문에
# 특정 FPS로 비디오를 재생하기 위해서는 별도의 구현이 필요하다.
# 이 코드에선 cv2.imshow 함수를 호출한 후 cv2.waitKey 함수에서 50 밀리초를 기다린다.
# 이미지를 표시하고 비디오를 디코딩하는데 소요되는 시간을 무시할수 있다고 가정하면
# 비디오는 20FPS 이하의 속도로 재생될 수 있다.