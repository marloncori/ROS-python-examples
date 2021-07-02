#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def subscriber():
    sub = rospy.Subscriber('/ir_publisher', String, print_result)
    rospy.spin()

def print_result(data):
    rospy.loginfo(data)

if __name__ == '__main__':
    rospy.init_node('ir_subscriber_node')
    subscriber()
