import json
import os
import cv2

f = open("giraffe.json", "r")

for line in f.readlines():
    js = json.loads(line)
    imgname = js["image_id"].split("/")[3] + ".JPG"
    img = cv2.imread("giraffes/" + imgname)
    label = open("labels/" + imgname.strip("JPG") + "txt", "a")
    h, w, c = img.shape
    x1, y1, wid, hei = js["bbox"]
    x1, y1, wid, hei = float(x1), float(y1), float(wid), float(hei)
    x1i, y1i, widi, heii = int(x1), int(y1), int(wid), int(hei)
    cv2.rectangle(img, (x1i,y1i), (x1i+widi,y1i+heii), (0,0,255), 10)
    img = cv2.resize(img, None, fx=0.3, fy=0.3)
    cv2.imshow("bounding box", img)
    cv2.waitKey(200)
    if input("Is this wrong? ") != "y":
        width = wid/w
        height = hei/h
        midx = str(x1/w + width/2)
        midy = str(y1/h + height/2)
        label.write("0 " + midx + " " + midy + " " + str(width) + " " + str(height) + "\n")
    label.close()


