import os

for fname in os.listdir("labels/"):
    f = open("labels/" + fname, "r")
    newf = open("newlabels/" + fname, "w")
    for line in f.readlines():
        l = line.split()
        l[0] = "0"
        newline = " ".join(l)
        newf.write(newline + "\n")
    f.close()
    newf.close()
