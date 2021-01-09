import cv2
import numpy as np

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

im = cv2.imread('F-22Raptor.jpg', -1)
img = ResizeWithAspectRatio(im, width=900, height=1000)

print(img.shape)

# img = cv2.line(img, (250,400), (500,600), (255,0,0), 5)
img = cv2.arrowedLine(img, (100,400), (235,285), (0,0,255), 4)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Wing', (45,450), font, 1.3, (0,0,255), 4, cv2.LINE_AA)

img = cv2.circle(img, (370,160), 45, (0,255,0), 5)
img = cv2.arrowedLine(img, (230,60), (370,160), (0,255,255), 4)
img = cv2.putText(img, 'Vertical Stabilizer', (30,40), font, 1.3, (0,255,0), 4, cv2.LINE_AA)

img = cv2.rectangle(img, (300,285), (500,390), (0,255,0), 5)
img = cv2.arrowedLine(img, (600,500), (400,345), (0,0,255), 4)
img = cv2.putText(img, 'Fuselage', (490,540), font, 1.3, (0,180,255), 4, cv2.LINE_AA)

img = cv2.arrowedLine(img, (720,130), (700,245), (0,0,255), 4)
img = cv2.putText(img, 'Horizontal Stabilizer', (480,120), font, 1.3, (0,0,255), 4, cv2.LINE_AA)

img = cv2.arrowedLine(img, (180,130), (200,190), (0,0,255), 4)
img = cv2.putText(img, 'Aileron', (130,120), font, 1.3, (0,255,255), 4, cv2.LINE_AA)

img = cv2.arrowedLine(img, (520,40), (380,90), (0,0,0), 4)
img = cv2.putText(img, 'Rudder', (530,40), font, 1.3, (235,235,225), 4, cv2.LINE_AA)

img = cv2.arrowedLine(img, (770,210), (690,310), (0,100,0), 4)
img = cv2.putText(img, 'Flaps', (745,200), font, 1.3, (235,235,225), 4, cv2.LINE_AA)

cv2.imshow('F-22 Raptor', img)
cv2.waitKey(0)
cv2.imwrite('F-22_Raptor_details.jpg', img)
cv2.destroyAllWindows()