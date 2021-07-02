#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
import RPi.GPIO as gpio

button_gpio = 16

def publisherMethod():
    rospy.init_node('rpi_button_state_pub')
    pub = rospy.Publisher('button_state', Bool, queue_size=10)

    gpio.setmode(gpio.BCM)
    gpio.setup(button_gpio, gpio.IN, pull_up_down = gpio.PUD_UP)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        gpio_state = not gpio.input(button_gpio)
        msg = Bool()
        msg.data = gpio_state
        pub.publish(msg)
        rate.sleep()

def endMethod():
    print("User has stopped the program").
    gpio.cleanup()

if __name__ == '__main__':
    try:
        publisherMethod()

    except KeyboardInterrupt:
        endMethod()
