import os

f = open("results.txt", "a")
for weightfile in os.listdir("test_weights"):
    thresh = [0.01, 0.25, 0.5, 0.6, 0.75]
    for t in thresh:
        f.write("************************************************************")
        f.write("********** weight file: " + weightfile + "**************")
        f.write("************** thresh = " + str(t) + " ********************")
        f.write("************************************************************")
        command = "./darknet detector map data/pb.data cfg/yolov3-pb.cfg test_weights/" + weightfile + " -thresh " + str(t) + " < data/test.txt >> results.txt"
        os.system(command)
