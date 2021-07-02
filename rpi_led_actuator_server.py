#!/usr/bin/env python
import rospy
from std_srvs.srv import SetBool
import RPi.GPIO as rp

rp_led = 20

def SetLedStateCallback(req):
    rp.output(rp_led, req.data)
    return ('success': True,
            'message': 'GPIO has succesfully changed LED state.')

def InitializeROSNode():
    rospy.init_node('led_actuator')
    
def RaspberryPiSetup():
    rp.setmode(rp.BCM)
    rp.setup(rp_led, rp.OUT)

def StartService():
    rospy.Service('set_led_state', SetBool, SetLedStateCallback)
    rospy.loginfo("Service server has started. Ready to get requests.")
    rospy.spin()

def FinishService():
    rospy.loginfo("User has stopped the service. Thank you by now'")
    rp.cleanup()

if __name__ == '__main__':
    try:
        InitializeROSNode()
        RasberryPiSetup()
        StartService()

    except KeyboardInterrupt:
        FinishService()
    
