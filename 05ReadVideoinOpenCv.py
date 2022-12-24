# reading video in opencv

import cv2 as cv 

cap = cv.VideoCapture('./resources/intro.mp4') 

if( cap.isOpened() == False):
    print("Video is not loaded")

# reading and playing video

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Video",frame)
        # when you pres Q video will be stoped
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break

cap.release()
cv.destroyAllWindows()
