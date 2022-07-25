import cv2

face = cv2.CascadeClassifier("~/src/frontalface.xml")
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(grey, 1.2, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Faces', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
