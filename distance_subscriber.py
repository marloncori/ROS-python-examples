#!/usr/bin/env python

import rospy
from actions_tutorial.smg import my_message

def subscriber():
    sub = rospy.Subscriber('string_publish', my_message, callback_function)
    rospy.spin()

def callback_function(msg):
    string_received = msg.data
    dist_received = msg.distance
    rospy.loginfo("Received message: %d" %dist_received)

def initializer():
    rospy.init_node('simple_subscriber')
    
if __name__ == '__main__':
    initializer()
    subscriber()
