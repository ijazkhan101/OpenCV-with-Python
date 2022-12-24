# Reading imag and displying it 
import cv2 as cv
from cv2 import cvtColor


img = cv.imread('resources/1stimg.jpg')
# resize img
img1 = cv.resize(img ,(800,600))


#Conversion 
gray_img = cvtColor(img,cv.COLOR_BGR2GRAY)

# diplay img
cv.imshow('1st Image',img)
cv.imshow('Gary img =',gray_img)

#Delay code 
cv.waitKey(0)
cv.destroyAllWindows()
