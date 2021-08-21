import cv2
import imutils
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(1)
# kernel = np.ones((5,5),np.uint8)
cap.set(3,640)
cap.set(6,480)
while True:
    success, image = cap.read()
    img = cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
    area = img[209: 328,132:403]
    depth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV32F
    gradX = cv2.Sobel(img,ddepth=depth,dx=1,dy=0,ksize=-1 )
    gradY = cv2.Sobel(img,ddepth=depth,dx=0,dy=1,ksize=-1 )

    gradient = cv2.subtract(gradX,gradY)
    gradient = cv2.convertScaleAbs(gradient)

    blurred = cv2.blur(gradient,(9,9))
    (,thresh) = cv2.threshold(blurred,255,255,cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(21,7))
    closed = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)

    closed = cv2.erode(closed,None,iterations=4)
    closed = cv2.dilate(closed,None,iterations=4)

    cnts = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for barcode in decode(img):
        print(barcode.data)
        mydata = barcode.data.decode('utf-8')
        print(mydata)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,255,0),5)
        pts2 = barcode.rect
        cv2.putText(img, mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,0,255),2)
    cv2.imshow('Result',img)
    # cv2.imshow("Laplacian",imgL)
    cv2.waitKey(1)