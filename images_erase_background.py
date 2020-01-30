# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 13:16:46 2020

@author: oscar
"""

from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse



img_object = cv.imread("spoon1.png", cv.IMREAD_COLOR)
img_scene= cv.imread("background.png", cv.IMREAD_COLOR)

img=img_object-img_scene



#img=cv.adaptiveThreshold(img_scene,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
_,img= cv.threshold(img_object, 10,150,cv.THRESH_BINARY)





#-- Show detected matches
cv.imshow('Good Matches & Object detection',img)
cv.waitKey()
