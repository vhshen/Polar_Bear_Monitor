import os

for f in os.listdir("train"):
    if "txt" in f:
        label = open("train/" + f, "r")
        newlabel = open("newlabel/" + f, "w")
        for line in label.readlines():
            l = line.split()
            l[0] = "0"
            w = " ".join(l)
            newlabel.write(w + "\n")
        label.close()
        newlabel.close()
            
