#!/usr/bin/env python3

import cv2

def main():

    #---------------------------------------------------
    #Initialization
    #---------------------------------------------------
    
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    #---------------------------------------------------
    #Execution
    #---------------------------------------------------
    
    _, image = capture.read()  # get an image from the camera

    #---------------------------------------------------
    #Visualisation
    #---------------------------------------------------

    cv2.imshow(window_name, image)  # Display the image

    #---------------------------------------------------
    #Termination
    #---------------------------------------------------
    
    cv2.waitKey(0)


    # add code to show acquired image
    # add code to wait for a key press

if __name__ == '__main__':
    main()