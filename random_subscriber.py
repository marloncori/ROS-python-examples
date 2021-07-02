#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo("This is the published random number: %s", data.data)

def randomSubscriber():
    rospy.init_node('random_subscriber')
    rospy.Subscriber('rand_num', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    randomSubscriber()
