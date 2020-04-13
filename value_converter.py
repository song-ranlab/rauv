#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import twist

temp_y = temp_z = 0


#to scale value
def scale(x)
    #a = x* factor
    # using the function x/sqrt(x^2 -1)
    num = x
    den = math.sqrt(math.pow(x,2) + 1)
    return num/den

#translating teleop output
def Twist(data)
    parameter = Parameter()

    if data.twist.linear.z != 0:
        #difference between current z value and previous value
        diff_z = data.twist.linear.z - temp_z
        #if user want to go in the positive z direction
        if data.twist.linear.z >= 0
            #PILOT_SPEED_UP parameter uses increments of 10
            parameter.z.inc = scale(diff_z) * 10
        #if user want to go in the negative z direction
        if data.twist.linear.z < 0
            #PILOT_SPEED_UP parameter uses increments of 10
            parameter.z.inc = scale(diff_z) * 10
        #set new temp value before scanning next parameter
        temp_z = data.twist.linear.z

    if data.twist.linear.y != 0:
        #difference between current z value and previous value
        diff_y = data.twist.linear.y - temp_z
        #if user want to go in the positive z direction
        if data.twist.linear.y >= 0
            #PILOT_SPEED_UP parameter uses increments of 10
            parameter.z.inc = scale(diff_z) * 10
        #if user want to go in the negative z direction
        if data.twist.linear.y < 0
            #PILOT_SPEED_UP parameter uses increments of 10
            parameter.y.inc = scale(diff_z) 
        #set new temp value before scanning next parameter
        temp_y = data.twist.linear.y



    pub.publish(parameter)


def start():
    # publishing to "parameter" to assign to Ardusub parameters
    global pub
    pub = rospy.Publisher('parameter', Parameter, queue_size=10)
    # subscribed to cmd_vel topic from the teleop node
    rospy.Subscriber("cmd_vel", Twist, Twist)
    # starts the node
    #rospy.init_node()
    rospy.spin()

if _name_ == '_main_'
    start()
