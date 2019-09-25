import os
import cv2

x1 = 0.3219
y1 = 0.7707
w1 = 0.55
h1 = 0.3634

x2 = 0.6487
y2 = 0.5335
w2 = 0.6213
h2 = 0.7729

img = cv2.imread("testimg.jpg")
h, w, c = img.shape
cv2.circle(img, (int(x1*w), int(y1*h)), 5, (255,0,0))
cv2.circle(img, (int(x2*w), int(y2*h)), 5, (0,255,0))

cv2.circle(img, (int(x1*w-(w1*w/2)), int(y1*h-(y1*h/2))), 5, (255,0,0))
cv2.circle(img, (int(x1*w+(w1*w/2)), int(y1*h-(y1*h/2))), 5, (255,0,0))
cv2.circle(img, (int(x1*w-(w1*w/2)), int(y1*h+(y1*h/2))), 5, (255,0,0))
cv2.circle(img, (int(x1*w+(w1*w/2)), int(y1*h+(y1*h/2))), 5, (255,0,0))

cv2.circle(img, (int(x2*w-(w2*w/2)), int(y2*h-(y2*h/2))), 5, (0,255,0))
cv2.circle(img, (int(x2*w+(w2*w/2)), int(y2*h-(y2*h/2))), 5, (0,255,0))
cv2.circle(img, (int(x2*w-(w2*w/2)), int(y2*h+(y2*h/2))), 5, (0,255,0))
cv2.circle(img, (int(x2*w+(w2*w/2)), int(y2*h+(y2*h/2))), 5, (0,255,0))

cv2.imshow("hello",img)
cv2.waitKey(0)
