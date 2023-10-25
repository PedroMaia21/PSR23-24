#!/usr/bin/env python3

import cv2
import argparse

def main():
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers')
    parser.add_argument('-ci', '--choose_image', type=int, help='number of image: choose between 1 and 5', required=True)

    args = vars (parser.parse_args())
    number = args['choose_image']

    if number == 1:
        image_filename = '/home/pedro/PSR23-24/2023-10-12_AulaP4/ImgLib/atlas2000_e_atlasmv_green_box_highlighted.png'
    elif number == 2:
        image_filename = '/home/pedro/PSR23-24/2023-10-12_AulaP4/ImgLib/atlas2000_e_atlasmv_green_segmentation.png'
    elif number == 3:
        image_filename = '/home/pedro/PSR23-24/2023-10-12_AulaP4/ImgLib/atlas2000_e_atlasmv.png'
    elif number == 4:
        image_filename = '/home/pedro/PSR23-24/2023-10-12_AulaP4/ImgLib/atlascar.png'
    elif number == 5:
        image_filename = '/home/pedro/PSR23-24/2023-10-12_AulaP4/ImgLib/atlascar2.png'
    else:
        print('Valor de entrada errado')
        return


    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()