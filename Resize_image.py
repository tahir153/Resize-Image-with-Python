import cv2

img = cv2.imread("picture")

Resized_img = cv2.resize(img, None, fx=0.45  , fy=0.45)
cv2.imshow("Resized image",Resized_img)
cv2.waitKey(0)