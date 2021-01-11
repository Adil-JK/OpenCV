import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img, points[-1], points[-2], (0,255,00), 3)
        cv2.imshow('image', img)

    if event== cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        colored_image = np.zeros((512,512,3), np.uint8)
        colored_image[:] = [blue, green, red]
        cv2.imshow('color', colored_image)

# img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('F-22_Raptor_details.jpg', -1)
cv2.imshow('image', img)
points = []

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

