# 프레임 스트림을 비디오로 저장
# USB 카메라에서 프레임을 실시간으로 캡처하는 방법과
# 지정된 비디오 코덱을 사용해 비디오 파일에 프레임을
# 동시에 저장하는 방법

import cv2
# 카메라 캡처 객체를 만들고 프레임 높이와 너비를 얻는다
capture = cv2.VideoCapture(0)
frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame width: ', frame_width)
print('Frame height: ', frame_height)

# 동영상 저장을 위한 비디오 라이터 객체를 생성
path = ('./data/drop.avi')
# 여기서 오류가 났었는데 h264 코덱의 dll 버전이 맞지 않다고
# 에러가 났었음
# 필요한 버전의 dll을 다운받아 파이썬 환경(가상환경) 폴더에
# 추가해주니 해결됨
video = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'X264'),
                        25, (frame_width, frame_height))

# while 루프에서 프레임을 캡처해 video.write 함수를 사용해
# 프레임을 저장한다
while True:
    has_frame, frame = capture.read()
    if not has_frame:
        print('Can\'t get frame')
        break

    video.write(frame)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(3)
    if key == 27:
        print('Pressed ESC')
        break

# 생성된 VideoCapture 와 VideoWriter 객체를
# 헤제하고 창을 닫는다
capture.release()
video.release()
cv2.destroyAllWindows()


# 비디오 쓰기는 cv2.VideoWriter 클래스를 사용해 수행
# 생성자는 출력 비디오 경로와 비디오 코드, 프레임 속도 및
# 프레임 크기를 지정하는 4개의 문자 코드(FOURCC)를 받는다
# 코덱 코드의 예에는
# MPEG-1 의 경우 P,I,M,1 이 포함되며
# M, J, P, G 는 모션-JPEG,
# XVID MPEG-4 에는 X, V, I, D이고
# H.264의 경우 H, 2, 6, 4를 포함한다

