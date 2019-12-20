import os
import shutil
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("old_dir", metavar="o", type=str, help="the directory with the images")
parser.add_argument("new_dir", metavar="n", type=str, help="the new directory to put into")
parser.add_argument("num_samples", metavar="s", type=int, help="the number of samples")
args = parser.parse_args()
odir = args.old_dir + "/"
if "//" in odir:
    odir = args.old_dir
ndir = args.new_dir + "/"
if "//" in ndir:
    ndir = args.new_dir
samp = args.num_samples

allnegs = []
for f in os.listdir(odir):
    if "jpg" in f:
        allnegs.append(f)

options = random.choices(allnegs, k=samp)
for s in options:
    if not os.path.exists(ndir + s):
        shutil.copy(odir + s, ndir + s)
        fname = s.strip("jpg") + "txt"
        shutil.copy(odir + fname, ndir + fname)
