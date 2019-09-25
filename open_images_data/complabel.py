import os
from os import path
import cv2
import numpy
import sys

for imagename in os.listdir("train/Polar_bear/images"):
    name = imagename.strip("jpg") + "txt"

    if not path.exists("train/Polar_bear/labels/" + name):
        print(imagename)
        if path.exists("oldlabels/" + name):
           print("old label file exists")

        img = cv2.imread("train/Polar_bear/images/" + imagename)
        h,w,c = img.shape

        txtpat = "oldlabels/" + name
        newtxtpat = "train/Polar_bear/labels/" + name

        old = open(txtpat, "r")
        new = open(newtxtpat, "w")
        for line in old.readlines():
            n1, n2, left, top, right, bottom = line.split()
            left, top, right, bottom = float(left), float(top), float(right), float(bottom)

            midx = ((right-left)/2+left)/w
            midy = ((bottom-top)/2+top)/h
            width = right/w - left/w
            height = bottom/h - top/h

            new.write("0 " + str(midx) + " " + str(midy) + " " + str(width) + " " + str(height) + "\n")
        old.close()
        new.close()

    
