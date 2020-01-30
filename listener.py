# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:17:33 2020

@author: oscar
"""

#!/usr/bin/env python


import cv2
from geometry_msgs.msg import Quaternion
import numpy as np
import rospy
import message_filters
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseStamped
from tf.transformations import *
from tf.msg import tfMessage
from tf.transformations import euler_from_quaternion
from cv_bridge import CvBridge, CvBridgeError
bridge = CvBridge()



from std_msgs.msg import String

def callback(img_msg):
    print( "got image")

    cv2_img = bridge.imgmsg_to_cv2(img_msg, "bgr8")
    print cv2_img.shape
    
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/hsrb/hand_camera/image_raw", Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
