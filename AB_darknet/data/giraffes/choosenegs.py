import os
import shutil
import random

allnegs = []
for f in os.listdir("../negs_test/"):
    if "jpg" in f:
        allnegs.append(f)

sampling = random.choices(allnegs, k=43)
for s in sampling:
    shutil.copy("../negs_test/" + s, "test/" + s)
    fname = s.strip("jpg") + "txt"
    shutil.copy("../negs_test/" + fname, "test/" + fname)
