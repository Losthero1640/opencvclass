import cv2 as cv
import numpy as np
img = cv.imread('photos/cat_large.jpg')
re_img = cv.resize(img, (500, 500))
h= np.hstack((re_img, re_img))
cv.imshow('Display', h)
cv.waitKey(0)