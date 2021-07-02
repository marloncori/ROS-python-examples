#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('string_publish!', String, queue_size = 10)
    rate = rospy.Rate(1)
    msg_publish = String()
    count = 0

    while not rospy.is_shutdown():
        string_publish = "Publishing counter: %d" %count
        count+=1

        msg_publish.data = string_publish
        rospy.longinfo(string_publish)
        rate.sleep()

def initializer():
    rospy.init_node("simple_publisher")


if __name__ == '__main__':
    try:
        initiliazer()
        publisher()

    except rospy.ROSInterruptException:
        pass
