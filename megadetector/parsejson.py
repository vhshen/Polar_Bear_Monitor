import json
import os
import cv2
import keyboard

f = open("output.json", "r")
full = f.read()

js = json.loads(full)
writer = open("err.txt", "w")
for name in os.listdir("../badlabels"):
    pth = "../data/" + name
    oimg = cv2.imread("../badlabels/" + name)
    img = cv2.resize(oimg, None, fx=0.3, fy=0.3)
    h, w, c = img.shape
    for i in js["images"]:
        if i["file"] == pth:
            for d in i["detections"]:
                x = int(d["bbox"][0]*w)
                y = int(d["bbox"][1]*h)
                cv2.circle(img, (x,y), 5, (255,0,0))
                cv2.imshow("meh", img)
                cv2.waitKey(500)
                if input("Was this the error? ") == "y":
                    writer.write(pth + "\n")
                    writer.write("conf: " + str(d["conf"]) + "\n")
                    writer.write("bbox: " + str(d["bbox"]) + "\n")
