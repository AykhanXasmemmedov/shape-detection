import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow('values')
cv2.createTrackbar('dp','values',12,30,nothing)
cv2.createTrackbar('param1','values',80,255,nothing)
cv2.createTrackbar('param2','values',20,255,nothing)
cv2.createTrackbar('kernel_size','values',3,51,nothing)
video=cv2.VideoCapture(0)
while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    size=cv2.getTrackbarPos('kernel_size','values')
    if size%2==0:
        size+=1
    blurring=cv2.GaussianBlur(gray,(size,size),0)
    dp=cv2.getTrackbarPos('dp','values')
    dp=dp/10
    param1=cv2.getTrackbarPos('param1','values')
    param2=cv2.getTrackbarPos('param2','values')
    circles=cv2.HoughCircles(blurring,cv2.HOUGH_GRADIENT,dp,20,param1=param1,param2=param2)
    number=0
    if circles is not None:
        circles=np.uint16(np.around(circles))

        for circle in circles[0,:]:
            number+=1
            x,y,r=circle
            cv2.circle(frame,(x,y),r,(0,255,0),2)
        cv2.putText(frame,'circle numbrs:{}'.format(number),(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,0),2)
    cv2.imshow('circles',frame)
    key=cv2.waitKey(10)
    if key==ord('q'):
        break
    elif key==ord('w'):
        cv2.waitKey(0)
    else:
        pass
video.release()
cv2.destroyAllWindows()