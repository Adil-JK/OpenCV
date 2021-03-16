import cv2
from gtts import gTTS
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
#img = cv2.imread('test.png')
vid = cv2.VideoCapture(0)

while vid.isOpened():
    _, frame = vid.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #frame = cv2.putText(frame, 'Muhammad Adil', (x, y+h+25), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        text = "Face detected"
        language = "en"
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("welcome.mp3")

        # Display the output
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()