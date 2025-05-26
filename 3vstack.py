import cv2 as cv
import numpy as np
img = cv.imread('photos/cat_large.jpg')
re_img = cv.resize(img, (300, 300))
h= np.vstack((re_img, re_img))
cv.imshow('Display', h)
cv.waitKey(0)