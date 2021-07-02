#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from random import randint

#define the random_number Publisher
def randomNumberPublisher():
    rospy.init_node('random_number')
    pub = rospy.Publisher('rand_num', Int32, queue_size=10)
    rate = rospy.Rate(2)

    #generate a random number every 2 secs
    while not rospy.is_shutdown():
        random_msg = randint(0,5000)
        rospy.loginfo(random_msg)
        pub.publish(random.msg)
        rate.sleep()

if __name__ == '__main__':
    ty:
        randomNumberPublisher()

    except rospy.ROSInterruptException:
        pass
