#!/usr/bin/env python
import rospy
import datetime

from tutorials2.msg import custom

def chatter():
    pub = rospy.Publisher("custom_message", custom)
    rospy.init_node("custom_talker", anonymous=True)
    r = rospy.Rate(10)

    msg = custom()
    msg.robot_name.data = "Hash robot"

    datetime_var = datetime.datetime.now()
    datetime_var = str(datetime_var)
    msg.date_time.data = datetime_var

    msg.location.x = 5
    msg.location.y = 5
    msg.location.theta = 90

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        chatter()

    except rospy.ROSInterruptException:
        pass
