import os
from os import path
import cv2
import numpy
import sys

for txtname in os.listdir("oldtestlabels"):
    name = txtname.strip("txt") + "jpg"

    if not path.exists("test/Polar_bear/images/" + name):
        print(txtname)
        os.remove("oldtestlabels/" + txtname)
