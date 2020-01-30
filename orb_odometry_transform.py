# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 13:16:46 2020

@author: oscar
"""

from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse



img_object = cv.imread("ref1.png", cv.IMREAD_COLOR)
img_scene= cv.imread("ref.png", cv.IMREAD_COLOR)
print (img_scene.shape)
detector = cv.ORB_create()

keypoints_obj, descriptors_obj = detector.detectAndCompute(img_object, None)

keypoints_scene, descriptors_scene = detector.detectAndCompute(img_scene, None)
np.save('kp_ref.npy',keypoints_scene)
np.save('des_ref.npy',descriptors_scene)
#-- Step 2: Matching descriptor vectors with a FLANN based matcher
# Since SURF is a floating-point descriptor NORM_L2 is used
#SINCE THIS CODE WAS MODIFIED FOR ORB HAMMING DISTANCE IS USED

matcher = cv.DescriptorMatcher_create(cv.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
matches = matcher.match(descriptors_obj,descriptors_scene,None)
matches.sort(key=lambda x: x.distance, reverse=False)
numGoodMatches = int(len(matches) * .30)
matches = matches[:numGoodMatches]
print (len(matches))
points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)
for i, match in enumerate(matches):
    points1[i, :] = keypoints_obj[match.queryIdx].pt
    points2[i, :] = keypoints_scene[match.trainIdx].pt
   
  # Find homography
h, mask = cv.findHomography(points1, points2, cv.RANSAC)
print(h)

imMatches= cv.drawMatches(img_object,keypoints_obj,img_scene,keypoints_scene, matches, None)

#-- Get the corners from the image_1 ( the object to be "detected" )
obj_corners = np.empty((4,1,2), dtype=np.float32)
obj_corners[0,0,0] = 0
obj_corners[0,0,1] = 0
obj_corners[1,0,0] = img_object.shape[1]
obj_corners[1,0,1] = 0
obj_corners[2,0,0] = img_object.shape[1]
obj_corners[2,0,1] = img_object.shape[0]
obj_corners[3,0,0] = 0
obj_corners[3,0,1] = img_object.shape[0]

scene_corners = cv.perspectiveTransform(obj_corners, h)

#-- Draw lines between the corners (the mapped object in the scene - image_2 )
cv.line(imMatches, (int(scene_corners[0,0,0] + img_object.shape[1]), int(scene_corners[0,0,1])),\
    (int(scene_corners[1,0,0] + img_object.shape[1]), int(scene_corners[1,0,1])), (0,255,0), 4)
cv.line(imMatches, (int(scene_corners[1,0,0] + img_object.shape[1]), int(scene_corners[1,0,1])),\
    (int(scene_corners[2,0,0] + img_object.shape[1]), int(scene_corners[2,0,1])), (0,255,0), 4)
cv.line(imMatches, (int(scene_corners[2,0,0] + img_object.shape[1]), int(scene_corners[2,0,1])),\
    (int(scene_corners[3,0,0] + img_object.shape[1]), int(scene_corners[3,0,1])), (0,255,0), 4)
cv.line(imMatches, (int(scene_corners[3,0,0] + img_object.shape[1]), int(scene_corners[3,0,1])),\
    (int(scene_corners[0,0,0] + img_object.shape[1]), int(scene_corners[0,0,1])), (0,255,0), 4)





#-- Show detected matches
cv.imshow('Good Matches & Object detection',imMatches)
cv.waitKey()
