import os

for fname in os.listdir("labels"):
    f = open("labels/" + fname, "r")
    iname = fname.strip("txt") + "JPG"
    if f.read() == "":
        os.rename("labels/" + fname, "unused/" + fname)
        #os.rename("images/" + iname, "unused/" + iname)
