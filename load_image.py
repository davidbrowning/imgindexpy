#1/usr/bin/python

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True, help = 'Path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

cv2.imshow('image', image)
cv2.waitKey(0)
