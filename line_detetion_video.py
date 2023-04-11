import numpy as np
import cv2
def nothing(x):
    pass
cv2.namedWindow('value')
cv2.createTrackbar('thresh','value',0,250,nothing)
cv2.createTrackbar('upH','value',0,180,nothing)
cv2.createTrackbar('downH','value',0,180,nothing)
cv2.createTrackbar('upS','value',0,255,nothing)
cv2.createTrackbar('downS','value',0,255,nothing)
cv2.createTrackbar('upV','value',0,255,nothing)
cv2.createTrackbar('downV','value',0,255,nothing)
video=cv2.VideoCapture(0)
while True:
    ret,frame=video.read()
    #cv2.imshow('video',frame)

    upH=cv2.getTrackbarPos('upH','value')
    upS=cv2.getTrackbarPos('upS','value')
    upV=cv2.getTrackbarPos('upV','value')
    downH=cv2.getTrackbarPos('downH','value')
    downS=cv2.getTrackbarPos('downS','value')
    downV=cv2.getTrackbarPos('downV','value')
    thresh=cv2.getTrackbarPos('thresh','value')


    blurring=cv2.GaussianBlur(frame,(3,3),0,borderType=cv2.BORDER_REFLECT)
    HSV=cv2.cvtColor(blurring,cv2.COLOR_BGR2HSV)
    upper_value=np.array([upH,upS,upV])
    down_value=np.array([downH,downS,downV])
    mask=cv2.inRange(HSV,down_value,upper_value)
    masking_frame=cv2.bitwise_and(frame,frame,mask=mask)
    canny=cv2.Canny(masking_frame,10,255,L2gradient=True)
    cv2.imshow('masking_frame',canny)
    lines=cv2.HoughLinesP(canny,1,np.pi/180,thresh,maxLineGap=10,minLineLength=10)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line[0]
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),3)
    cv2.imshow('frame',frame)
    key=cv2.waitKey(100)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
