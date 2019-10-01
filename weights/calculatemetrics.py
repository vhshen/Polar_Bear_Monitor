import os
import re

res = open("results.txt", "r")
metrics = open("metrics.txt", "w")
fullres = res.read()
sections = fullres.split("******************************************************************\n***")
start = 0

highest_map = 0.0
hmap_name = "hello"
hthresh = 0.0
second_map = 0.0
smap_name = "hi"
hthresh2 = 0.0
for s in sections:
    if not (start):
        start = 1
        continue

    wname = re.search("(?<=weight file: )\w*.\w*", s).group(0)
    thresh = re.search("(?<=thresh: )\w*.\w*", s).group(0)
    TP = re.search("(?<=TP = )\d*", s).group(0)
    FP = re.search("(?<=FP = )\d*", s).group(0)
    FN = re.search("(?<=FN = )\d*", s).group(0)
    F1 = re.search("(?<=F1-score = )0.\d*", s).group(0)
    
    precision = re.search("(?<=precision = )\d.\d*", s).group(0)
    recall = re.search("(?<=recall = )\d.\d*", s).group(0)
    avg_iou = re.search("(?<=average IoU = )\d*.\d*", s).group(0)
    avg_prec = re.search("(?<=\(mAP@0.50\) = )\d.\d*", s).group(0)
    
    if float(avg_prec) > float(highest_map):
        highest_map = avg_prec
        hmap_name = wname
        hthresh = thresh
    elif float(avg_prec) == float(highest_map) and hmap_name != smap_name:
        second_map = avg_prec
        smap_name = wname
        hthresh2 = thresh

    metrics.write("File name: " + wname + "\n")
    metrics.write("threshold: " + thresh + "\n\n")
    metrics.write("AB calculated precision: " + precision + "\n")
    metrics.write("AB calculated recall: " + recall + "\n")
    metrics.write("AB calculated avg_IoU: " + avg_iou + "\n")
    metrics.write("AB calculated mAP: " + avg_prec + "\n")
    metrics.write("AB calculate F1-score: " + F1 + "\n\n")
    metrics.write("Truth: 81 detections\n")
    metrics.write("TP: " + TP + "\tFP: " + FP + "\tFN: " + FN + "\n")

    TPi, FPi, FNi = float(TP), float(FP), float(FN)
    prec = TPi/(TPi + FPi)
    rec = TPi/(TPi + FNi)
    F1s = 2*(prec*rec/(prec+rec))

    metrics.write("My calculated precision: " + str(prec) + "\n")
    metrics.write("My calculated recall: " + str(rec) + "\n")
    metrics.write("My F1 score: " + str(F1s) + "\n")
    metrics.write("******************************************************\n")

print("Highest map is: " + highest_map + " for weight file: " + hmap_name + " with thresh: " + hthresh)
print("Tied is: " + second_map + " for weight file: " + smap_name + " with thresh: " + hthresh2)
