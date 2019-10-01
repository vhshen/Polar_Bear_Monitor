Iterations:

    1. unclean_openimages: scraped openimages then trained on original darknet branch. No modifications.
    2. clean_openimages: deleted the toy/non-polar bear images from openimages pictures. Added negative images from the VOC dataset, and also added images of snow/snowmen.
    3. AB_openimages_pb: trained on Cheetah Chin with the AlexeyAB branch. Trained with the same data as the previous iteration (all real polar bear images + negatives). All backup weights files still on cheetahchin
    4. AB_probably_openimages_pb: can't figure out where this weights file comes from. High mAP though...
    5. megalabels: megan's data, labelled with the megadetector with a threshold of 92%. no manual labelling, sent directly to train with the negative VOC images.
    6. manlabels: megan's data, labelled with the megadetector at the default threshold (80%) and then gone through manually to check the labels. also traine with negative VOC images.
