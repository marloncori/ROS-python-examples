#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def subscriberCallback(data):
    rospy.loginfo(rospy.get_caller_id() + "I have received -- %s", data.data)

def listener():
    rospy.init_node('subscriberNode', anonymous=True)
    rospy.Subscriber('babbler', String, subscriberCallback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
