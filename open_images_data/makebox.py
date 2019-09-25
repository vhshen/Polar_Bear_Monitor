import os
from os import path
import cv2

for f in os.listdir("train/Polar_bear/images"):
    name = f.strip("jpg") + "txt"
    if not path.exists("oldlabels/" + name):
        continue
    old = open("oldlabels/" + name, "r")

    img = cv2.imread("train/Polar_bear/images/"+f)
    h, w, c = img.shape

    for line in old.readlines():
        polar, bear, left, top, right, bottom = line.split()
        left, top, right, bottom = float(left), float(top), float(right), float(bottom)
        midx = ((right-left)/2+left)/w
        midy = ((bottom-top)/2+top)/h
        width = right/w-left/w
        height = bottom/h-top/h
        left, top, right, bottom = int(left), int(top), int(right), int(bottom)
        cv2.circle(img, (left, top), 5, (255,0,0))
        cv2.circle(img, (left, bottom), 5, (255,0,0))
        cv2.circle(img, (right, top), 5, (255,0,0))
        cv2.circle(img, (right, bottom), 5, (255,0,0))

    cv2.imshow("hello",img)
    cv2.waitKey(0)
    old.close()
