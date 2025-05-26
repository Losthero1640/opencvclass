import cv2 as cv
import numpy as np
img = cv.imread('photos/cat_large.jpg')
re_img = cv.resize(img, (300, 300))
h= np.hstack((re_img, re_img))
v= np.vstack((h,h))
cv.imshow('Display', v)

cv.waitKey(0)