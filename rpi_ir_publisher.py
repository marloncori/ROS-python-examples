#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
import time

ir_sensor = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(ir_sensor,GPIO.IN)

def publisher():
    pub = rospy.Publisher('/ir_publisher', String, queue_size = 10)
    rate = rospy.Rate(1)
    message = String()
    while not rospy.is_shutdown():
        if GPIO.input(ir_sensor) == 1:
            message.data = "Object not detected."

        else:
            message.data = "Object detected."

        pub.publish(message)
        rate.sleep()
    rospy.loginfo("Node has stopped")


if __name__ == '__main__':
    try:
        rospy.init_node('ir_publisher_node')
        publisher()

    except rospy.ROSInterruptException:
        pass
