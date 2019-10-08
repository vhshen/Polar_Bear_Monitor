import os

for imgname in os.listdir("test/"):
    fname = imgname.strip("JPG") + "txt"
    os.rename("labels/" + fname, "test/" + fname)
