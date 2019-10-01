import os
import cv2

for name in os.listdir("labels"):
    imgname = name.strip("txt") + "jpg"
    if not os.path.exists("data/" + imgname):
        imgname = imgname.strip("jpg") + "jpeg"
    print(name)
    img = cv2.imread("data/" + imgname)
    h, w, c = img.shape
    if h > 1000 or w > 1000:
        img = cv2.resize(img, None, fx=0.3, fy=0.3)
        h, w, c = img.shape
    label = open("labels/" + name, "r")
    for line in label.readlines():
        name, midx, midy, wid, hei = line.split()
        midx, midy, wid, hei = float(midx), float(midy), float(wid), float(hei)
        x1 = int(midx*w - wid*w/2)
        x2 = int(midx*w + wid*w/2)
        y1 = int(midy*h - hei*h/2)
        y2 = int(midy*h + hei*h/2)
        cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255))
#        cv2.imshow("hello", img)
#        cv2.waitKey(0)
        cv2.imwrite("vislabels/"+imgname, img)
    label.close()
