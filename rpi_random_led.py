#!/usr/bin/env python
 
import rospy
 
from std_msgs.msg import Int32
from std_msgs.msg import String

var = None

def callback(msg):
    global var
    var = msg.data

def publishSubscribe():
    rospy.init_node('random_led')
    rospy.Subscriber('random_number', Int32, callback)
    pub = rospy.Publisher('LED', String, queue_size=1)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if var <= 2500:
            #send message to turn off LED
            varP = "OFF"
            rospy.loginfo("The output is OFF and the var is: %s", var)

        else:
            varP = "ON"
            rospy.loginfo("The output os ON and the var is: %s", var)

    pub.publish(varP)
    rate.sleep()

if __name__ == '__nain__':
    try:
        publishSuscriber()

    except rospy.ROSInterruptException:
        pass
