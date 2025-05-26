import cv2 as cv

img = cv.imread('photos/cat_large.jpg')
re_img = cv.resize(img, (500, 500))
cv.imshow('Display', re_img)
cv.waitKey(0)