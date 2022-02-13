# https://analyticsindiamag.com/converting-image-into-a-pencil-sketch-in-python/

import cv2

image = cv2.imread('img/003.jpg')

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_invert = cv2.bitwise_not(image_gray)

image_smoothing = cv2.GaussianBlur(image_invert, (21, 21),sigmaX=0, sigmaY=0)

pencil_sketch = cv2.divide(image_gray, 255 - image_smoothing, scale=256)


cv2.imshow('pencil_sketch', pencil_sketch)
cv2.waitKey()

cv2.destroyAllWindows()