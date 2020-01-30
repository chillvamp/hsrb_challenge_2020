# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:24:30 2019

@author: oscar
"""

import cv2 
import numpy as np
global circles

cam = cv2.VideoCapture(0)
backSub = cv2.createBackgroundSubtractorMOG2()
while True:
    # Read each frame in video stream
    ret, frame = cam.read()
    # Display each frame in video stream
    
    cap_cnt=0
    
    fgMask = backSub.apply(frame)

    
    
    
    
    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgMask)
    
    
    
    
    if not ret:
        break
# Monitor keystrokes
    k = cv2.waitKey(1)

    if k & 0xFF == ord('q'):
        # q key pressed so quit
        print("Quitting...")
        cv2.destroyAllWindows()
        break
    elif k & 0xFF == ord('c'):
        # c key pressed so capture frame to image file
        cap_name = "capture_{}.png".format(cap_cnt)
        cv2.imwrite(cap_name, frame)
        print("Saving {}!".format(cap_name))
        # Increment Capture Counter for next frame to capture
        cap_cnt += 1
cam.release()
print('Released')
    