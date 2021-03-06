# -*- coding: utf-8 -*-

#!/usr/bin/env python
import time
import roslib
import math
import rospy
import cv2
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

from Classes import robot_location, image_converter
from Vision import findCentroid, closestBall, image2global
from Control import PI_control, Fetch

if __name__ == '__main__':
    robot = robot_location()  
    ic = image_converter()
    rospy.init_node('image_converter', anonymous=True)

    rospy.Subscriber("/camera/rgb/image_color",Image,ic.callback)
    rospy.Subscriber('/RosAria/pose', Odometry, robot.odometry)
    time.sleep(1)    

    robot.mark()    
    
    pub_cmd = rospy.Publisher('/RosAria/cmd_vel', Twist, queue_size=1000)
    
    global ori_sum ; ori_sum = 0
    (Cx,Cy,radius) = 0,0,0
    Ready = False
    cleaned = False
    
    while not rospy.is_shutdown():
        time.sleep(0.01)
        #try:
        (Cx,Cy)=  closestBall() 
        #except:
        #    no ball in vision: (Cx,Cy) = (250,-999)
        Cx -= 25
        print"Cx,Cy=",Cx,Cy
        (X,Y) = image2global(Cx, Cy)
        print"\n\n X,Y",X,Y
        
        if Cy == -999:	# no ball in vision
        	cleaned = spinAround(robot, Cx, Cy, pub_cmd)
        	
        elif Cy > 0:        
            if Ready == False:
                Ready = PI_control(Cx,Cy)                    
            elif Ready == True:
                print "Fetch"              
                Fetch(robot, pub_cmd)
                Ready = False

        
# x right
# y down
# z outward


    
    
    
    
