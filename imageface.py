import cv2

def imageface(img):
    face = cv2.CascadeClassifier("frontalface.xml")
    cap = cv2.imread(img)
    grey = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(grey, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(cap, (x, y), ((x+w), (y+h)), (0, 255, 0), 2)
    i = cv2.resize(cap , (1080, 720), interpolation = cv2.INTER_LINEAR)
    cv2.imwrite("Output/face4detected.jpg", cap)
    cv2.imshow("Result", i)
    k = cv2.waitKey(0)
    
img = str(input("Enter the filename with extension"))
imageface(str(img))
print("Result stored in Output folder!")
