import os
import cv2

xmin = 0.6125789284
ymin = 0.262260705
width = 0.2894194722175598
height = 0.48310616612434387

name = "IMG_9487_2.txt"
imgname = name.strip("txt") + "jpg"
aimg = cv2.imread(imgname)
img = cv2.resize(aimg, None, fx=0.3, fy=0.3)
h, w, c = img.shape
label = open(name, "r")
for line in label.readlines():
    print(line)
    name, midx, midy, wid, hei = line.split()
    midx, midy, wid, hei = float(midx), float(midy), float(wid), float(hei)
    x1 = int(midx*w - wid*w/2)
    x2 = int(midx*w + wid*w/2)
    y1 = int(midy*h - hei*h/2)
    y2 = int(midy*h + hei*h/2)
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255))
    cv2.rectangle(img, (int(xmin*w), int(ymin*h)), (int((xmin+width)*w), int((ymin+height)*h)), (0,255,0))
    cv2.imshow("hello", img)
    cv2.waitKey(0)
label.close()
