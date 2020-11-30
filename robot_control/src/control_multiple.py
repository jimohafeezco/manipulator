#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import math

def joint_name(number):
    name = '/manipulator/joint'+ str(number)+ '_position_controller/command'
    return name

def talker():
    # pub_joint3 = rospy.Publisher('/manipulator/joint2_position_controller/command', Float64, queue_size=10)
    joints= []
    pub= []
    total_joints = 6

    for i in range(total_joints):
        joints.append(joint_name(i+1))
        pub.append(rospy.Publisher(joints[i], Float64, queue_size=10))   

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(50) 
    start =0.0
    while not rospy.is_shutdown():    
        pos =math.cos(start)*1.57    
        rospy.loginfo("started publishing")
        for j in range(total_joints):
            pub[j].publish(pos)
        start+=0.025

    rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass