import cv2
import numpy as np

img = cv2.imread("C:/Coding/SOA/pic/t1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 120)
minLineLength = 50000000
maxLineGap = 5
lines = cv2.HoughLinesP(edges, 1.0, np.pi / 180, 20, minLineLength, maxLineGap)
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

cv2.imshow("lines", img)
cv2.waitKey()
cv2.destroyAllWindows()
