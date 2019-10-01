import json
import os
import cv2
import keyboard

f = open("output.json", "r")
full = f.read()

js = json.loads(full)
for i in js["images"]:
    name = i["file"].split("/")[2].strip("jpg") + "txt"
    print(name)
    label = open("labels/" + name, "w")
    for d in i["detections"]:
        if d["category"] == "1":
            midx = str(float(d["bbox"][0]) + float(d["bbox"][2])/2)
            midy = str(float(d["bbox"][1]) + float(d["bbox"][3])/2)
            label.write("polar_bear " + midx + " " + midy + " " + str(d["bbox"][2]) + " " + str(d["bbox"][3]) + "\n")

    label.close()
f.close()    
