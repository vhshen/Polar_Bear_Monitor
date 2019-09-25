import json
import os
import cv2
import keyboard

f = open("output.json", "r")
full = f.read()

js = json.loads(full)
for name in os.listdir("../data"):
    pth = "../data/" + name
    oimg = cv2.imread(pth)
    img = cv2.resize(oimg, None, fx=0.3, fy=0.3)
    h, w, c = img.shape
    for i in js["images"]:
        if i["file"] == pth:
            label = open("../labels/" + name.strip("jpg") + "txt", "w")
            for d in i["detections"]:
                x1 = int(d["bbox"][0]*w)
                y1 = int(d["bbox"][1]*h)
                x2 = x1 + int(d["bbox"][2]*w)
                y2 = y1 + int(d["bbox"][3]*h)
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255))
                cv2.imshow("image", img)
                cv2.waitKey(200)
                if input("Is this wrong? ") != "y":
                    midx = str(d["bbox"][0] + d["bbox"][2]/2)
                    midy = str(d["bbox"][1] + d["bbox"][3]/2)
                    label.write("polar_bear " + midx + " " + midy + " " + str(d["bbox"][2]) + " " + str(d["bbox"][3]) + "\n")
            label.close()
f.close()
