#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
import RPi.GPIO as pi

led_pi = 20

def buttonStateCallback(msg):
    pio.output(led_pi, msg.data)

def subscriberMethod()
    rospy.init_node('rpi_led_actuator')
    pi.setmode(pi.BCM)
    pi.setup(led_pi, pi.OUT)
    rospy.Subscriber('button_state', Bool, buttonStateCallback)
    rospy.spin()

def closeMethod()
    print("User has stopped the program.")
    pi.cleanup()


if __name__ == '__main__':
    try:
        subscriberMethod()

    except KeyboardInterrupt:
        closeMethod()
