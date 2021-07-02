#!/usr/bin/env python
import rospy
from std_srvs.srv import SetBool
import RPi.GPIO as rpi

rpi_button = 16

def ButtonCallback(channel):
    switch_on_led = not rpi.input(rpi_button)

    rospy.wait_for_service('rpi_led_actuator_server')
    try:
        set_led_state = rospy.ServiceProxy('set_led_state', SetBool)
        resp = set_led_state(switch_on_led)
    except rospy.ServiceException, e:
        rospy.logwarn(e)

def InitializeROSNode():
    rospy.init_node('led_actuator')
    
def RaspberryPiSetup():
    rpi.setmode(rp.BCM)
    rpi.setup(rpi_button, rpi.IN, pull_up_down = rpi.PUD_UP)

def ClientMethod():
    rpi.add_event_detect(rpi_button, rpi.BOTH, callback=ButtonCallback, bouncetime=50)
    rospy.spin()

def FinishService():
    rospy.loginfo("User has stopped the service. Thank you by now'")
    rp.cleanup()

if __name__ == '__main__':
    try:
        InitializeROSNode()
        RasberryPiSetup()
        ClientMethod()

    except KeyboardInterrupt:
        FinishService()
    
