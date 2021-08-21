import cv2

cam =cv2.VideoCapture(1)

face_haarcascade = cv2.CascadeClassifier("D:\\16 Hrithik\\ml\\day 1\\haarcascade_frontalface_default.xml")

# while True:
#     msg, img = cam.read()
#     face_coordinate = face_haarcascade.detectMultiScale(img, 1.4, 10)
#     print(face_coordinate)
#     for x, y, w, h in face_coordinate:  #since more than one face
#         cv2.rectangle(img, (x, y),(x+w, y+h), (255, 255, 255), 2)
#     cv2.imshow('image', img)
#     key = cv2.waitKey(10)
#     if key == 32:
#         break



while True:
    msg, img = cam.read()
    if msg:
        face_coordinates = face_haarcascade.detectMultiScale(img, 1.2, 10)
        print(face_coordinates)

        for x, y, w, h in face_coordinates:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Face detection", img)
        key = cv2.waitKey(10)
        if key == 32:
            break
    else:
        print('check camera status')