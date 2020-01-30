# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:24:30 2019

@author: oscar
"""

import cv2 
import numpy as np
global circles
global frame
global maxrad

frame=np.load('imagen.npy')


def on_trackbar(val):
    global gray
    value=val
    img = cv2.medianBlur(frame,5)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, val, 100)

    print (circles)
    if circles is not None:
        print ("found")
	# convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        

        for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(gray, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(gray, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    
    cv2.imshow("chidalavida", gray)
    



    #circles_callback()
    
def Whooopss_callback():
    
    print (circles)    
    
    
    
    



while True:
    
    
    # Read each frame in video stream
   
    #ret,thresh1 = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
    
    
    cv2.namedWindow("chidalavida")
    cv2.createTrackbar("circs", "chidalavida" , 0, 200  , on_trackbar)
    
#    cv2.createTrackbar("max_rad", "chidalavida" , 0, 600  , maxrad_trackbar)    
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

print('Released')
    