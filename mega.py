import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(6,480)
while True:
    success, image = cap.read()
    imgGray = cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
    img = cv2.GaussianBlur(imgGray,(7,7),0)
    for barcode in decode(img):
        print(barcode.data)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,255,0),5)
        mydata = barcode.data.decode('utf-8')
        print(mydata)
    cv2.imshow('Result',img)
    cv2.waitKey(1)
    key = cv2.waitKey(10)
    if key == 32:
        break
else:
    print('check camera status')