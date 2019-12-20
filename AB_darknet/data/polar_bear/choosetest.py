import os
import shutil
import random

allnegs = []
for f in os.listdir("manlabels_megandata/negs"):
    if "txt" not in f:
        allnegs.append(f)

i=0
sampling = random.choices(allnegs, k=35)
for s in sampling:
    if os.path.exists("manlabels_megandata/test/" + s):
        continue
    i += 1
    if "jpg" in s:
        fname = s.strip("jpg") + "txt"
    else:
        fname = s.strip("jpeg") + "txt"
    os.rename("manlabels_megandata/negs/" + s, "manlabels_megandata/test/" + s)
    os.rename("manlabels_megandata/negs/" + fname, "manlabels_megandata/test/" + fname)

print(i)
