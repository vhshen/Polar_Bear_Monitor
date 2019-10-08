import os
import cv2
import json

f = open("giraffe.json", "r")
for line in f.readlines():
    js = json.loads(line)
    imgname = js["image_id"].split("/")[3] + ".JPG"
    x1, y1, w, h = js["bbox"]
    x1, y1, w, h = int(x1), int(y1), int(w), int(h)
    img = cv2.imread("giraffes/" + imgname)
    cv2.rectangle(img, (x1,y1), (x1+w,y1+h), (0,0,255), 10)
    img = cv2.resize(img, None, fx=0.3, fy=0.3)
    cv2.imshow("hello", img)
    cv2.waitKey(0)
