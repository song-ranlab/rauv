#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    twist = Twist()
    twist.linear.x = data.axes[1]
    twist.linear.y = data.axes[0]
    twist.linear.z = data.axes[4]
    twist.angular.z = data.axes[3]    
    pub.publish(twist)


def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joy2Tele')
    rospy.spin()

if __name__ == '__main__':
    start()
