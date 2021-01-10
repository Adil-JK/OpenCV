import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        date_time = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame, date_time, (10,40), font, 1, (0,255,0), 2, cv2.LINE_AA)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()