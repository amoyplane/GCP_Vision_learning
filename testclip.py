import cv2
import numpy as np

img = cv2.imread("C:/Coding/SOA/pic/t3.jpg")
# print(img.shape)

cropped = img[10:100, 10:100]
cv2.imshow("show", cropped)
cv2.waitKey(0)
cv2.imwrite("ans2.jpg", cropped)
