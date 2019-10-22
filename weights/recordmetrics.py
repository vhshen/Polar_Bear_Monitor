import os

wfolder = "../weights/"

tiny = False
o = open("order.txt", "w")
for weightfile in os.listdir(wfolder):
    if "weights" not in weightfile:
        continue
    print("Weightfile: " + weightfile)

    animal, rest = weightfile.split("_")
    if "tiny" in animal:
        tiny = True
        animal = animal.split("-")[1]
    
    o.write("weight file: " + weightfile + "\n")
    if tiny:
        command = "./darknet detector map data/" + animal + ".data cfg/yolov3-tiny-custom.cfg " + wfolder + weightfile + " < data/"+ animal + "test.txt >> results.txt"
    else:    
        command = "./darknet detector map data/" + animal + ".data cfg/yolov3-custom.cfg " + wfolder + weightfile + " < data/"+ animal + "test.txt >> results.txt"
    os.system(command)
