#!/usr/bin/env python3

import cv2
from functools import partial
import numpy as np

def mouseCallback(event, x, y, flags, *userdata, image, drawingData):
    if event == cv2.EVENT_LBUTTONDOWN:
        drawingData['pencilDown'] = True

    elif event == cv2.EVENT_LBUTTONUP:
        drawingData['pencilDown'] = False
    
    if drawingData['pencilDown'] == True:
        print(drawingData['color'])
        startCoordinates = (drawingData['previousX'],drawingData['previousY'])
        color = drawingData['color']
        thickness = 3

        image = cv2.line(image,startCoordinates, (x,y), color, thickness)

    drawingData['previousX'] = x
    drawingData['previousY'] = y


def main():
    
    image = np.ones((400,600,3),dtype=np.uint8)*255

    drawingData = {'pencilDown': False, 'previousX':0, 'previousY':0, 'color': (255,255,255)}
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", partial(mouseCallback, image = "image", drawingData = drawingData))
    h,w,nc = image.shape
    centerCoordinates = (int(w/2),int(h/2))
    radius = 55
    color = (255,0,0)
    thickness = 3

    textToWrite='PSR'
    bottomCoordinates = (int(w/2),h)
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 3
    colorText = (0,0,255)
    thickness = 3

    image = cv2.circle(image,centerCoordinates, radius, color, thickness)
    image = cv2.putText(image, textToWrite, bottomCoordinates, font, scale, colorText, thickness)
    
    while True:
        cv2.imshow('image', image)  # Display the image
        key = cv2.waitKey(50) # wait for a key press before proceeding
        if key == ord('q'):
            print('Quitting programm')
            break
        elif key == ord('r'):
            drawingData[color]=(0,0,255)
        elif key == ord('g'):
            drawingData[color]=(0,255,0)
        elif key == ord('b'):
            drawingData[color]=(255,0,0)

if __name__ == '__main__':
    main()