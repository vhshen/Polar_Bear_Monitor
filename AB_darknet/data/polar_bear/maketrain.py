import os
import random

folders = ["test", "negs_test"]
writefile = "test.txt"

allf = []
for f in folders:
    pth = "data/polar_bear/" + f + "/"
    for fname in os.listdir(f):
        if "txt" not in fname:
            allf.append(pth + fname + "\n")

random.shuffle(allf)
w = open(writefile, "w")
for l in allf:
    w.write(l)
w.close()
