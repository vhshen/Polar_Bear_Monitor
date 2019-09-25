import os

for f in os.listdir("."):
    if "jpetxt" in f:
        newname = f.split(".")[0] + ".txt"
        os.rename(f, newname)
