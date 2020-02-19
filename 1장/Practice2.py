import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='./data/Lena.png',
                    help='input image path')
parser.add_argument('--out_png', default='./data/Lena_compressed.png',
                    help='output image path for lossless result')
parser.add_argument('--out_jpg', default='./data/Lena_compressed.jpg',
                    help='output image path for lossy result')
params = parser.parse_args()
img = cv2.imread(params.path)
print(img.shape)
# 화질 손실 없이 PNG 형식으로 이미지를 저장한 다음 다시 읽어 들여
# 디스크에 저장하는 동안 모든 정보가 보존됐는지 확인

# 낮은 압축률로 이미지를 저장, 파일 크기는 크지만 디코딩이 빠름
cv2.imwrite('data/Lena_compressed.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 5])

# 이미지를 저장하고 다시 불러들여 원본과 동일한지 비교한다
saved_img = cv2.imread(params.out_png)
print(saved_img.shape)
assert saved_img.all() ==img.all()

# 이미지를 낮은 화질로 저장한다. - 크기가 더 작아진다
cv2.imwrite('data/Lena_compressed.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 0])
print(cv2.imread(params.out_jpg).shape)

# 이미지를 저장하기 위해 cv2.imwrite 함수를 사용.
# cv2.imwrite 함수는 출력파일의 경로, 이미지, 저장 매개변수의 세가지 인자를 받는다
# png 형식으로 이미지를 저장할때는 압축 수준을 지정할 수 있다. (0~9)
# 숫자가 클수록 디스크의 파일 크기는 작지만 디코딩 프로세스가 느려진다
# jpeg 형식은 0에서 100사이의 값으로 지정가능 (더 큰값이 좋은 품질의미)

orig = cv2.imread(params.path)
orig_size = orig.shape[0:2]
print(orig_size)

cv2.imshow('Original image', orig)
# 첫번째 매개변수는 창의 이름, 두번째는 표시할 이미지
cv2.waitKey(2000)
# waitKey는 창의 표시 시간을 제어


# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# import argparse
# import cv2
#
# parser = argparse.ArgumentParser()
# parser.add_argument( '--path', default='./data/Lena.png', help='Image path.' )
# parser.add_argument( '--iter', default=50, help='Downsampling-upsampling iterations number.' )
# params = parser.parse_args()
# orig = cv2.imread( params.path )
# orig_size = orig.shape[0:2]
#
# cv2.imshow( "Original image", orig )
# cv2.waitKey( 2000 )
#
# resized = orig
#
# for i in range( params.iter ):
#     resized = cv2.resize( cv2.resize( resized, (256, 256) ), orig_size )
#     cv2.imshow( "downsized&restored", resized )
#     cv2.waitKey( 100 )
#
# cv2.destroyWindow( "downsized&restored" )
#
# cv2.namedWindow( "original", cv2.WINDOW_NORMAL )
# cv2.namedWindow( "result" )
# cv2.imshow( "original", orig )
# cv2.imshow( "result", resized )
# cv2.waitKey( 0 )
#
# cv2.destroyAllWindows()


