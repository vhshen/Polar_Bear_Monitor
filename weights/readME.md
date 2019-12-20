## This folder contains all the yolov3 weights files trained on darknet.
#### The actual weights files themselves can be found on cheetah@cheetahchin, or on Ian's SD card.

Abbreviation Definitions:

	* oi = data came from [open images](https://storage.googleapis.com/openimages/web/index.html) and then put through megadetector
	* ss = data came from [snapshot serengeti](https://www.zooniverse.org/projects/zooniverse/snapshot-serengeti) and then put through megadetector
	* nonAB = the weights file was NOT trained on the AlexeyAB branch (default: most of them were trained w/ AlexeyAB)
	* manlabels (also DEFAULT for oi/ss files) = the openimages files were put through megadetector (80% threshold) and then I manually went through them to delete the incorrect labels
	* megalabels = the openimages files were put through megadetector (92% threshold) and then immediately went through training (no manual inspection)

Notes:
	* all the weights were trained with NEGATIVE images (from the Pascal VOC dataset), 1:1 ratio with positives.
	* when training with openimages data, went through data beforehand and deleted all non-real pictures (i.e. polar bear toys, etc.)
	* the polar bear weights without oi label were trained using data from Megan only
	* the "extras" folder contains the iterations from training on okapitongue. delete-able/redundant files, mostly.

