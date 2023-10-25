#!/usr/bin/env python3

import cv2
import numpy as np
import argparse


# Global variables
window_name = 'window - Ex3a'
image_gray = None


def onTrackbar(threshold):
    retified_threshold = int(threshold/100*255) #Translates percentage to 0 - 255 value
    retval, image_thresholded = cv2.threshold(image_gray, retified_threshold, 255, cv2.THRESH_BINARY) #change the image
    cv2.imshow(window_name, image_thresholded) #show the changed image


def main():
    #------------------------
    # Initialization
    #------------------------
    
    parser = argparse.ArgumentParser() #Creates an required argument of the image path
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image

    #------------------------
    # Execution
    #------------------------

    global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converts to gray scale
    retval, image_thresholded = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY) #Gets a threshold of the grey image
    cv2.namedWindow(window_name) #Create the window

    cv2.createTrackbar('Threshold Value', window_name, 50, 100, onTrackbar)

    #------------------------
    # Visualization
    #------------------------

    cv2.imshow(window_name, image_thresholded)  # Display the image

    #------------------------
    # Termination
    #------------------------
    
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()