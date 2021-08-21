import cv2
###1

img = cv2.imread("D:\\16 Hrithik\\ml\\day 1\\tum.jpg")
print(img)
cv2.imshow("Image", img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", img_gray)
cv2.waitKey(5000)

###2
#
# cam = cv2.VideoCapture(0)
# while True:
#     msg, img = cam.read()
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Image", img_gray)
#     key = cv2.waitKey(10)
#     if key == 32:
#         break
#     print(key)


####3

# img = cv2.imread("D:\\16 Hrithik\\ml\\day 1\\tum.jpg")
# cv2.imshow("Image", img)
# cv2.rectangle(img, (200, 200),(400, 350), (255, 0, 0), 2)
# cv2.imshow("Image", img)
# cv2.waitKey(0)

# cam = cv2.VideoCapture(0)
# msg, img = cam.read()
# while True:
#     msg, img = cam.read()
#     cv2.rectangle(img, (200, 200), (400, 350), (255, 0, 0), 2)
#     cv2.imshow("Image", img)
#     key = cv2.waitKey(10)

###4 (use of msg)
# cam = cv2.VideoCapture(0)
# msg, img = cam.read()
# print(msg)
# key = cv2.waitKey(10)