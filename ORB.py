# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:03:09 2020

@author: oscar
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('capture_0.png',0)
print(img.shape)
# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)
print(kp)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
# draw only keypoints location,not size and orientation

img2 = cv2.drawKeypoints(img, kp, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img2),plt.show()
