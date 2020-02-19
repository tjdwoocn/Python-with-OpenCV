# 사용자의 키보드 입력 처리

import argparse
import cv2, random
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='./data/Lena.png', help='image path')
params = parser.parse_args()
img = cv2.imread(params.path)
image_to_show = np.copy(img)
w, h = img.shape[1], img.shape[0]

def rand_pt():
    return (random.randrange(w),
            random.randrange(h))

# 사용자가  P, L, R, E, T 를 누르면 각각 점, 선, 사각형, 타원, 텍스트를 그린다
# 또한 사용자가 D 를 누르면 그려진 프리미티브가 지워지고 Esc 키를 누르면 프로그램이 종료된다

finish = False
while not finish:
    cv2.imshow('result', image_to_show)
    key = cv2.waitKey(0)
    if key == ord('p'):
        for pt in [rand_pt() for _ in range(10)]:
            cv2.circle(image_to_show, pt, 3, (255,0,0), -1)
    elif key == ord('l'):
        cv2.line(image_to_show, rand_pt(), rand_pt(), (0,255,0), 3)
    elif key == ord('r'):
        cv2.rectangle(image_to_show, rand_pt(), rand_pt(), (0,0,255), 3)
    elif key == ord('e'):
        cv2.ellipse(image_to_show, rand_pt(), rand_pt(), random.randrange(360),
                    0, 360, (255,255,0), 3)
    elif key == ord('t'):
        cv2.putText(image_to_show, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 0), 5)
    elif key == ord('d'):
        image_to_show = np.copy(img)
    elif key == 27:
        finish = True