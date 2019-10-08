import os

for f in os.listdir("plains2"):
    if os.path.exists("plains/" + f):
        print(f)
        os.remove("plains2/" + f)
