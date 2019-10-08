import os

for f in os.listdir("plains_test/"):
    newname = f.strip("jpg") + "txt"
    newf = open("labels/" + newname, "w")
    newf.close()

