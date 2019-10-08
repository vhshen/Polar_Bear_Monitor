import json
import os
import cv2
import argparse

# boolean variables
imagedir = "."
labeldir = "."
newlabeldir = "."

# initiate parser
parser = argparse.ArgumentParser()
parser.add_argument("imagedir", metavar="imageDIR", type=str, help="directory with original images")
parser.add_argument("labeldir", metavar="labelDIR", type=str, help="directory with generated labels")
parser.add_argument("newlabeldir", metavar="newlabelDIR", type=str, help="directory to put manually annotated labels")
args = parser.parse_args()
imagedir = args.imagedir + "/"
if "//" in imagedir:
    imagedir = args.imagedir
labeldir = args.labeldir + "/"
if "//" in labeldir:
    labeldir = args.labeldir
newlabeldir = args.newlabeldir + "/"
if "//" in newlabeldir:
    newlabeldir = args.newlabeldir

for imgname in os.listdir(imagedir):
    namel = imgname.split(".")
    namel[len(namel)-1] = "txt"
    fname = (".").join(namel)
    img = cv2.imread(imagedir + imgname)
    h, w, c = img.shape
    if h > 1000 or w > 1000:
        img = cv2.resize(img, None, fx=0.3, fy=0.3)
        h, w, c = img.shape
    lab = open(labeldir + fname, "r")
    newlab = open(newlabeldir + fname, "w")
    for line in lab.readlines():
        classname, xmid, ymid, wid, hei = line.split()
        xmid, ymid, wid, hei = float(xmid), float(ymid), float(wid), float(hei)
        x1 = int((xmid-wid/2)*w)
        y1 = int((ymid-hei/2)*h)
        x2 = int((xmid+wid/2)*w)
        y2 = int((ymid+hei/2)*h)
        cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255))
        cv2.imshow("image", img)
        cv2.waitKey(200)
        if input("Is this wrong? ") != "y":
            newlab.write(line)
    lab.close()
    newlab.close()


