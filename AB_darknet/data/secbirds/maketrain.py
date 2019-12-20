import os

w = open("train.txt", "w")
for f in os.listdir("train"):
    pth = "data/secbirds/train/"
    if "txt" not in f:
        w.write(pth + f + "\n")
