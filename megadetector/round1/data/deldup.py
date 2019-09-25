import os
from os import path

for f in os.listdir("."):
    name = f.split(".")[0]
    newname = name + ".jpg"
    os.rename(f, newname)
