# img convert into black and white 
import cv2 as cv
import cv2
from cv2 import imwrite 

img = cv.imread('resources/1stimg.jpg')

#Conversion 
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh , binary)= cv.threshold(gray,127,255,cv.THRESH_BINARY)
# diplay img
cv.imshow('orginal',img)
cv.imshow('Gary img =',gray)


cv.imshow('black and white img ',binary)

imwrite('binary.png',gray)
#Delay code 
cv.waitKey(0)
cv.destroyAllWindows()
