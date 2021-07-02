#my_message.msg
strin data
int32 distance

#!/usr/bin/env python

import rospy
from actions_tutorial.msg import my_message

def publishMethod():
    pub = rospy.Publisher('string_publisher', my_message, queue_size=10)
    rate = rospy.Rate(1)
    msgPublish = my_message()

    distance = 70
    while not rospy.is_shutdown():
        stringPublish = "The distance to obstacle is %d meters" %distance
        distance -=2

        msgPublish.data = stringPublish
        msgPublish.distance = distance
        pub.publish(msgPublish)
        rate.sleep()

def initializer():
    rospy.init_node("distance_publisher")


if __name__ == '__main__':
    try:
        initiliazer()
        publishMethod()

    except rospy.ROSInterruptException:
        pass
