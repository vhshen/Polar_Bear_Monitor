import os

for f in os.listdir("test"):
    iname = f.strip("JPG") + "txt"
    os.rename("labels/" + iname, "test/" + iname)
