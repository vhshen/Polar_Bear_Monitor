import os

lbls = open("train.txt", "a")
for f in os.listdir("snow"):
    lbls.write("/home/vivian/data/OIDv4_Toolkit/OID/Dataset/train/Polar_bear/images/")
    lbls.write(f)
    lbls.write("\n")
    newname = f.strip("jpg") + "txt"
    newf = open("labels/" + newname, "w")
    newf.close()

for f in os.listdir("snowman"):
    lbls.write("/home/vivian/data/OIDv4_Toolkit/OID/Dataset/train/Polar_bear/images/")
    lbls.write(f)
    lbls.write("\n")
    newname = f.strip("jpg") + "txt"
    newf = open("labels/" + newname, "w")
    newf.close()

lbls.close()
