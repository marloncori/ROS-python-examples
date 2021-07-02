#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def subscriber():
    sub = rospy.Subscriber('string_publish', String, callback_function)
    rospy.spin()

def callback_function(msg):
    rospy.loginfo("I received the following: %s" %msg.data)

def initializer():
    rospy.init_node('simple_subscriber')
    
if __name__ == '__main__':
    initializer()
    subscriber()
