import os
from os import path
import cv2

for f in os.listdir("train/Polar_bear/images"):
    name = f.strip("jpg") + "txt"
    if not path.exists("oldlabels/" + name):
        continue
    new = open("train/Polar_bear/labels/" + name, "r")

    img = cv2.imread("train/Polar_bear/images/"+f)
    h, w, c = img.shape

    for line in new.readlines():
        a, midx, midy, width, height = line.split()
        midx, midy, width, height = float(midx), float(midy), float(width), float(height) 
        left = (midx-width/2)*w
        right = (midx+width/2)*w
        top = (midy-height/2)*h
        bottom = (midy+height/2)*h
        left, top, right, bottom = int(left), int(top), int(right), int(bottom)
        cv2.circle(img, (left, top), 5, (255,0,0))
        cv2.circle(img, (left, bottom), 5, (255,0,0))
        cv2.circle(img, (right, top), 5, (255,0,0))
        cv2.circle(img, (right, bottom), 5, (255,0,0))

    cv2.imshow("hello",img)
    cv2.waitKey(0)
    new.close()
