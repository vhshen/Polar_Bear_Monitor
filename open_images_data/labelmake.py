import cv2
import numpy
import sys
import os

for imagename in os.listdir("validation/Polar_bear/images"):
    print(imagename)
    img = cv2.imread("validation/Polar_bear/images/" + imagename)
    h,w,c = img.shape

    txtname = imagename.strip("jpg") + "txt"
    txtpat = "validation/Polar_bear/labels/" + txtname
    newtxtpat = "validation/Polar_bear/newlabels/" + txtname

    old = open(txtpat, "r")
    new = open(newtxtpat, "a")
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

    
