import os

writer = open("train.txt", "w")
pth = "data/polar_bear/train/"
for f in os.listdir("/home/vivian/data/OIDv4_Toolkit/OID/Dataset/train/Polar_bear/images"):
    writer.write(pth)
    writer.write(f)
    writer.write("\n")

writer.close()
