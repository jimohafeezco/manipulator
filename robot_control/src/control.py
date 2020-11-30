#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import math

def talker():
    pub_joint3 = rospy.Publisher('/manipulator/joint2_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(50) 
    start =0.0
    while not rospy.is_shutdown():    
        pos =math.sin(start)        
        rospy.loginfo("started publishing")
        pub_joint3.publish(pos)
        start+=0.025

    rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass