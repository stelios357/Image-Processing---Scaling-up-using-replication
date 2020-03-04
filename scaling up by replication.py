
"""/*
 *	scaling up by replication.py
 *	Created on: feb 12 , 2020
 *		Author:	Aman Jain
                18dcs009
                Aman Pawha
                18dcs013
 *
 *
 *	~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
 *	This program is designed to demonstrate keyboard handling in
 *	opencv.
 *	Give the image name in the argument else it will take defualt
 *	image.
 *	~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
 *
 */
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt



print("Please drag the mouse pointer and make a box in image window . New window will open of the same size but with zoomedin image .")
print()
print("Press ctrl+C to see final image . Ctrl+r to release selection ")
print()
print("You have to run again once made a selection and seen final image.")
print()
print("You have to run again once made a selection and seen final image.")






refPt = []
cropping = False


def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


img = image = cv2.imread('op.jpg')

b, g, r = cv2.split(img)

or_w, or_h, channel = img.shape

print("Enter the factor you want to scale up by(via replication):")

x = y = int(input())

new_b1 = np.zeros((or_w * x, or_h), np.uint8)
new_g1 = np.zeros((or_w * x, or_h), np.uint8)
new_r1 = np.zeros((or_w * x, or_h), np.uint8)

for i in range(x):
    new_b1[i::x, ::] = b
    new_g1[i::x, ::] = g
    new_r1[i::x, ::] = r

new_b2 = np.zeros((or_w * x, or_h * y), np.uint8)
new_g2 = np.zeros((or_w * x, or_h * y), np.uint8)
new_r2 = np.zeros((or_w * x, or_h * y), np.uint8)

for i in range(x):
    new_b2[::, i::y] = new_b1
    new_g2[::, i::y] = new_g1
    new_r2[::, i::y] = new_r1

final_img = np.zeros((or_w * x, or_h * y, channel), np.uint8)

final_img[:, :, 0] = new_b2
final_img[:, :, 1] = new_g2
final_img[:, :, 2] = new_r2

print("original image shape:", img.shape)
print("resize image shape:", final_img.shape)

# construct the argument parser and parse the arguments

# load the image, clone it, and setup the mouse callback function
clone = final_img.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break
# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
    roi = clone[refPt[0][1]*x:refPt[1][1]*y, refPt[0][0]*x:refPt[1][0]*y]
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)
# close all open windows
cv2.destroyAllWindows()
