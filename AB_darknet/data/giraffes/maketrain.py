import os

w = open("test.txt", "w")
for f in os.listdir("test"):
    pth = "data/giraffes/test/"
    if "txt" not in f:
        w.write(pth + f + "\n")
