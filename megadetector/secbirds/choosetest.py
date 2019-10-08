import os
import shutil
import random

allimgs = []
for f in os.listdir("images"):
    allimgs.append(f)

sampling = random.choices(allimgs, k=4)
for s in sampling:
    os.rename("images/" + s, "test/" + s)
