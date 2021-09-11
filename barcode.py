import cv2
import imutils
import numpy as np
from pyzbar.pyzbar import decode, ZBarSymbol

def unsharp_mask(image, kernel_size=(5,5), sigma=20, amount=1, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened


cap = cv2.VideoCapture(1)
# kernel = np.ones((5,5),np.uint8)
cap.set(3,640)
cap.set(6,480)
while True:
    success, image = cap.read()
    img = cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
    sharpened_image = unsharp_mask(img)
    area = img[209: 328,132:403]
    depth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV32F
    gradX = cv2.Sobel(img,ddepth=depth,dx=1,dy=0,ksize=-1 )
    gradY = cv2.Sobel(img,ddepth=depth,dx=0,dy=1,ksize=-1 )

    gradient = cv2.subtract(gradX,gradY)
    gradient = cv2.convertScaleAbs(gradient)

    blurred = cv2.blur(gradient,(9,9))
    (_,thresh) = cv2.threshold(blurred,255,255,cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(21,7))
    closed = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)

    closed = cv2.erode(closed,None,iterations=4)
    closed = cv2.dilate(closed,None,iterations=4)

    cnts = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for barcode in decode(sharpened_image,symbols=[ZBarSymbol.QRCODE]):
        print(barcode.data)
        mydata = barcode.data.decode('utf-8')
        print(mydata)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(sharpened_image,[pts],True,(255,255,0),5)
        pts2 = barcode.rect
        cv2.putText(sharpened_image, mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,0,255),2)
    cv2.imshow('Result',sharpened_image)
    # cv2.imshow("Laplacian",imgL)
    cv2.waitKey(1)