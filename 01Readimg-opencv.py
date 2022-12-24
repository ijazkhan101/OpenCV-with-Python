# Reading imag and displying it 
import cv2 as cv

img = cv.imread('resources/1stimg.jpg')

# resize img
img1 = cv.resize(img ,(800,600))


cv.imshow('1st Image',img)
cv.imshow('Resize img 1st Image',img1)



cv.waitKey(0)
