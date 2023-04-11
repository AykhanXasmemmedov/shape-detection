import cv2
import numpy as np

def nothing(x):
    pass
cv2.namedWindow('values')
cv2.createTrackbar('blocksize','values',1,27,nothing)#for gaussian kernel size
cv2.createTrackbar('threshlow','values',0,255,nothing) #for Canny low threeshold
cv2.createTrackbar('thresh','values',0,300,nothing)#for threshold value of hough lines P 
cv2.createTrackbar('min line Length','values',0,200,nothing)# min line length of hough lines
cv2.createTrackbar('maxlineGap','values',0,200,nothing) #maxlinegap parameter in hough lines
#///////////////////////////////////////////////////////////////////////////////////////////////
video=cv2.VideoCapture(0)
while True:
    ret,frame=video.read()        
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #///////////////////////////////////////////////////////
    size=cv2.getTrackbarPos('blocksize','values')
    if size%2==0:
        size+=1   
    blurring=cv2.GaussianBlur(gray,(size,size),0)
    cv2.imshow('blurring',blurring)
    #//////////////////////////////////////////////////////
    low=cv2.getTrackbarPos('threshlow','values')
    canny=cv2.Canny(blurring,low,255)
    #/////////////////////////////////////////////////////
    thresh=cv2.getTrackbarPos('thresh','values')
    linelength=cv2.getTrackbarPos('min line Length','values')
    maxlinegab=cv2.getTrackbarPos('maxlineGap','values')
    lines=cv2.HoughLinesP(canny,1,np.pi/180,thresh,minLineLength=linelength,maxLineGap=maxlinegab)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line[0]
            cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),3)

    #////////////////////////////////////////////////////////     
    cv2.imshow('orginal',frame)    
    cv2.imshow('image',canny)
    key=cv2.waitKey(10)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()





