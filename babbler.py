#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def publishMethod():
    pub = rospy.Publisher('babbler', Float64, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        publishString = 32
        rospy.loginfo("Data is being sent...")
        pub.publish(publishString)
        rate.sleep()

if __name__ == '__main__':
    try:
        publishMethod()

    except rospy.ROSInterruptException:
        pass
