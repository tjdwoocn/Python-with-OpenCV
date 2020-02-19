# 2D 프리미티브 그리기: 마커, 선, 타원, 사각형 및 텍스트

import argparse
import cv2, random

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='./data/Lena.png', help='image path')
params = parser.parse_args()
img = cv2.imread(params.path)

w, h = img.shape[1], img.shape[0]

# 이미지 내부에서 임의의 점을 반환하는 함수
def rand_pt(mult=1):
    return(random.randrange(int(w*mult)),
           random.randrange(int(h*mult)))

# 원 그리기
cv2.circle(img, rand_pt(), 40, (255, 0, 0))
cv2.circle(img, rand_pt(), 5, (255, 0, 0), cv2.FILLED) # 원 안의 공간 채우기
cv2.circle(img, rand_pt(), 60, (255, 85, 85), 5) # 원의 크기와 두께
cv2.circle(img, rand_pt(), 100, (255, 170, 170), 3, cv2.LINE_AA) # 앨리어스가 없는 경계를 지정

# 선그리기
cv2.line(img, rand_pt(), rand_pt(), (0, 255, 0))
cv2.line(img, rand_pt(), rand_pt(), (85, 255, 85), 3)
cv2.line(img, rand_pt(), rand_pt(), (170, 255, 170), 3, cv2.LINE_AA) # 앨리어싱을 억제

# 화살표 그리기
cv2.arrowedLine(img, rand_pt(), rand_pt(), (0, 0, 255), 3, cv2.LINE_AA)

# 사각형 그리기
cv2.rectangle(img, rand_pt(), rand_pt(), (255, 255, 0), 5)

# 타원 그리기
cv2.ellipse(img, rand_pt(), rand_pt(0.7), random.randrange(360),
            0, 360, (255, 255, 255), 30)
# ellipse는 이미지, (x,y) 형식의 중심 위치, (a,b) 형식의 반축 길이, 회전각도,
# 그리기 시작 각도, 그리기 끝 각도, 색상 및 선 두께를 매개변수로 받음

# 이미지에 텍스트 표시
cv2.putText(img, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX, 3,
            (250, 20, 20), 6)
# 이미지, 배치할 텍스트, 텍스트의 좌하단 위치, 글꼴명, 심볼의 스케일, 색상, 선두께다)



cv2.imshow('result', img)
cv2.waitKey(0)