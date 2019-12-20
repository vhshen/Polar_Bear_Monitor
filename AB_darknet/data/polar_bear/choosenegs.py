import os
import shutil
import random

origf = "negs_train/"
newf = "throwaway/"
samplesize = 10

allnegs = []
for f in os.listdir(origf):
    if "txt" not in f:
        allnegs.append(f)

i=0
sampling = random.choices(allnegs, k=samplesize)
for s in sampling:
    if os.path.exists(newf + s):
        continue
    i += 1
    if "jpg" in s:
        fname = s.strip("jpg") + "txt"
    else:
        fname = s.strip("jpeg") + "txt"
    os.rename(origf + s, newf + s)
    os.rename(origf + fname, newf + fname)

print(i)
