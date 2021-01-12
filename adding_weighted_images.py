import cv2
import numpy as np

img = cv2.imread("F-16.jpeg")
img2 = cv2.imread("Flag.jpg")

print(img.shape)
print(img2.shape)

img = cv2.resize(img, (1280,800))
img2 = cv2.resize(img2, (1280,800))

cmb = cv2.addWeighted(img, 0.8, img2, 0.2, 0)
cv2.imshow('Image', cmb)

filename = "newimage.jpg"
cv2.imwrite(filename, cmb)

cv2.waitKey(0)
cv2.destroyAllWindows()