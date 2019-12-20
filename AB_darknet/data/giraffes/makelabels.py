import os
for f in os.listdir("plains/"):
    name = f.strip("jpg") + "txt"
    lab = open("plains/" + name, "w")
    lab.close()

