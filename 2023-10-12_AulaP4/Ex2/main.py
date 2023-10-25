#!/usr/bin/env python3

import cv2
import numpy as np

def main():
    
    image_filename = '/home/pedro/PSR23-24/2023-10-12_AulaP4/ImgLib/atlas2000_e_atlasmv.png'

    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    retval, image_thresholded = cv2.threshold(image_grey, 128, 255, cv2.THRESH_BINARY)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    b, g, r = cv2.split(image)
    h, s, v = cv2.split(image_hsv)

    bmin, gmin, rmin = (0, 50, 0)
    bmax, gmax, rmax = (50, 255, 50)
    hmin, smin, vmin = (35, 100, 50)
    hmax, smax, vmax = (85, 255, 255)


    retval2, image_blue = cv2.threshold(b, 50, 255, cv2.THRESH_BINARY)
    retval3, image_green = cv2.threshold(g, 100, 255, cv2.THRESH_BINARY)
    retval4, image_red = cv2.threshold(r, 150, 255, cv2.THRESH_BINARY)

    result_image = cv2.merge((image_blue,image_green,image_red))

    lower_bound = np.array([bmin, gmin, rmin], dtype=np.uint8)
    upper_bound = np.array([bmax, gmax, rmax], dtype=np.uint8)
    lower_bound_hsv = np.array([hmin, smin, vmin], dtype=np.uint8)
    upper_bound_hsv = np.array([hmax, smax, vmax], dtype=np.uint8)
    mask = cv2.inRange(image, lower_bound, upper_bound)
    mask2 = cv2.inRange(image_hsv, lower_bound_hsv, upper_bound_hsv)
    segmented_image = cv2.bitwise_and(image, image, mask=mask)
    segmented_image_hsv = cv2.bitwise_and(image_hsv, image_hsv, mask=mask2)

    image_red_box = np.zeros_like(image)
    image_red_box[mask > 0] = (0,0,255)
    image_red_box = cv2.add(image, image_red_box)

  

    cv2.imshow('window1', image)  # Display the image
    cv2.imshow('window2', image_grey)  # Display the image
    cv2.imshow('window3', image_thresholded)  # Display the image
    cv2.imshow('window4', result_image)  # Display the image
    cv2.imshow('window5', segmented_image)  # Display the image
    cv2.imshow('window6', mask)
    cv2.imshow('window7', mask2)
    cv2.imshow('window9', image_red_box)
    cv2.imshow('window8', segmented_image_hsv)
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()