import cv2 as cv

# img=cv.imread('photos/cat_large.jpg')

# cv.imshow('Display', img)

# cv.waitKey(0)  


capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    cv.imshow('Video', frame)
    
    
    if cv.waitKey(10) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()