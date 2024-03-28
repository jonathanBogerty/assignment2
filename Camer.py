import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
cam=cv2.VideoCapture(0)
while True:
    ret,image=cam.read()
    image=cv2.resize(image, (640, 480))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,120,180)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 100, None, 0, 0)
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(image, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
            cv2.imshow("hough transform", image)
    cv2.imshow("Camera", edges)
    k=cv2.waitKey(1)
    if k==27:
        break
cam.release()
cv2.destroyAllWindows