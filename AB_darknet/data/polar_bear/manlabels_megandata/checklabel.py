import os

for f in os.listdir("train"):
    if "jpg'" in f:
        fname = f.strip("jpg'") + "txt'"
        if not os.path.exists("train/" + fname):
            os.rename("train/" + f, "nolabel/" + f)
    elif "jpg" in f:
        fname = f.strip("jpg") + "txt"
        if not os.path.exists("train/" + fname):
            os.rename("train/" + f, "nolabel/" + f)
    if "jpeg" in f:
        fname = f.strip("jpeg") + "txt"
        if not os.path.exists("train/" + fname):
            os.rename("train/" + f, "nolabel/" + f)
