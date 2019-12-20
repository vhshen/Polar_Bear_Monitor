import os
import shutil
import random

i = 0
allnegs = []
for f in os.listdir("../negs_test/"):
    if "jpg" in f:
        allnegs.append(f)
        i += 1

options = random.choices(allnegs, k=10)
for s in options:
    if not os.path.exists("test/" + s):
        shutil.copy("../negs_test/" + s, "test/" + s)
        fname = s.strip("jpg") + "txt"
        shutil.copy("../negs_test/" + fname, "test/" + fname)
