#!/usr/bin/env python3

import cv2
import numpy as np
import argparse
from functools import partial


def onTrackbar(threshold, image_data):
    black_withe_thr = cv2.getTrackbarPos('Threshold Value', image_data['window_name'])
    retval, image_thresholded = cv2.threshold(image_data['image'], black_withe_thr, 255, cv2.THRESH_BINARY) #change the image
    cv2.imshow(image_data['window_name'], image_thresholded) #show the changed image

    min_blue_hue_thr = cv2.getTrackbarPos('Min B/H', image_data['window_name'])
    min_green_sat_thr = cv2.getTrackbarPos('Min G/S', image_data['window_name'])
    min_red_val_thr = cv2.getTrackbarPos('Min R/V', image_data['window_name'])
    max_blue_hue_thr = cv2.getTrackbarPos('Max B/H', image_data['window_name'])
    max_green_sat_thr = cv2.getTrackbarPos('Max G/S', image_data['window_name'])
    max_red_val_thr = cv2.getTrackbarPos('Max R/V', image_data['window_name'])
   
    _,image_blue_hue = cv2.threshold(image_data['bh'], min_blue_hue_thr, max_blue_hue_thr, cv2.THRESH_BINARY)
    _,image_green_sat = cv2.threshold(image_data['gs'], min_green_sat_thr, max_green_sat_thr, cv2.THRESH_BINARY)
    _,image_red_val = cv2.threshold(image_data['rv'], min_red_val_thr, max_red_val_thr, cv2.THRESH_BINARY)

    image_thresholded_2 = cv2.merge((image_blue_hue,image_green_sat,image_red_val))

    cv2.imshow(image_data['window_name']+' Merge', image_thresholded_2)
    cv2.imshow(image_data['window_name']+' Blue / Hue', image_blue_hue)
    cv2.imshow(image_data['window_name']+' Green / Saturation', image_green_sat)
    cv2.imshow(image_data['window_name']+' Red / Value', image_red_val)

def onMouseCallback(event, x, y, *userdata, image_data):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x: '+str(x)+'   y:'+str(y))


def main():
    #------------------------
    # Initialization
    #------------------------
    
    parser = argparse.ArgumentParser() #Creates an required argument of the image path
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.') #path to image argument
    parser.add_argument('-hs', '--hsv', required=False, help='Use to transform in hsv mode',action='store_true')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image

    if args['hsv']:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        bh, gs, rv = cv2.split(image)
    else:
        bh, gs, rv = cv2.split(image)


    #------------------------
    # Execution
    #------------------------

    image_data = {'window_name':'Ex3', 'image': 0, 'hsv':args['hsv'], 'bh':bh, 'gs':gs, 'rv':rv}
    image_data['image'] = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converts to gray scale
    retval, image_thresholded = cv2.threshold(image_data['image'], 128, 255, cv2.THRESH_BINARY) #Gets a threshold of the grey image
    cv2.namedWindow(image_data['window_name']) #Create the window

    cv2.createTrackbar('Threshold Value', image_data['window_name'], 129, 255, partial(onTrackbar, image_data=image_data))#Creates the first trackbar
    cv2.setMouseCallback(image_data['window_name'],partial(onMouseCallback, image_data=image_data)) #Executes the mouse callback function

            #MOREEEE TRACKBARS
    cv2.createTrackbar('Min B/H', image_data['window_name'], 50, 255, partial(onTrackbar, image_data=image_data))#Creates the first trackbar
    cv2.createTrackbar('Max B/H', image_data['window_name'], 255, 255, partial(onTrackbar, image_data=image_data))#Creates the first trackbar
    cv2.createTrackbar('Min G/S', image_data['window_name'], 50, 255, partial(onTrackbar, image_data=image_data))#Creates the first trackbar
    cv2.createTrackbar('Max G/S', image_data['window_name'], 255, 255, partial(onTrackbar, image_data=image_data))#Creates the first trackbar
    cv2.createTrackbar('Min R/V', image_data['window_name'], 50, 255, partial(onTrackbar, image_data=image_data))#Creates the first trackbar
    cv2.createTrackbar('Max R/V', image_data['window_name'], 255, 255, partial(onTrackbar, image_data=image_data))#Creates the first trackbar
    

    #------------------------
    # Visualization
    #------------------------

    cv2.imshow(image_data['window_name'], image_thresholded)  # Display the image

    #------------------------
    # Termination
    #------------------------
    
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()