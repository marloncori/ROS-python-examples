#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

distToObstacle = 1

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + " The distance to obstacle is - %s", msg.ranges[300])

    #if dist in front of robot is higher than 1 m, the robot will move forward
    if msg.ranges[300] > distToObstacle:
        move.linear.x = 0.5
        move.angular.z = 0.0

    #if dist lower then 1m, turn left
    if msg.ranges[300] <= distToObstacle:
        move.linear.x = 0.0
        move.angular.z = 0.5

    pub.publish(move)

def pub_sub_method():
    rospy.init_node('sub_node')
    sub = rospy.Subscriber('/scan', LaserScan, callback)
    pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=2)
    rate = rospy.Rate(2)
    move = Twist()
    rospy.spin()

if __name__ == '__main__':
    try:
        pub_sub_method()
        
    except rospy.ROSInterruptException:
        pass
