#according to parameter thruster will move auv 50 cm/s

import rospy
import math

#following mission path on 
#https://docs.google.com/presentation/d/1byiLI5PmSsF17uo3vu67g_D1zAS3xIYWgthhTiYyXOI/edit#slide=id.g6c44cb7098_37_23

from geomtry_msgs.msg import Twist

def main():
    while != rospy.is.shutdown:
        t = 0
        time_move_to_gate = timecalc(3, 0.5)
        # moving to
        while t < time_move_to_gate:

            data.x = 0;
            data.y = 1;
            data.z = 0;
            moving(data)
            #update condition
            t += 1

# Opening gate code would go here

        #moving towards marker
        t = 0;
        time_move_to_marker  = timecalc(10,0.5)
        while t<time_move_to_marker:
            data.x = 0;
            data.y = 1;
            data.z = 0;

            t += 1

        while t< time_to_uturn:
            #data.xy.angular = math.cos(x)
            data.xy.angular = 1;


    pun.publish(twist)

# Printing string command for simulator
def moving(data)
    twist = twist()

    #twist.mode = "guided"
    twist.x.translate = data.x
    twist.y.translate = data.y
    twist.z.translate = data.z
    twist.xy.rotate = data.xy_angular


#def moving(data):
        #para = parameter()

        #para.m = ("mode guide")
        #para.x = twist.x
        #para.v =  "velocity {} {} {}".format(data.x,data.y,data.z)
        #para.sy = "setyaw {} {} {}".format(data.yaw_angle, data.yaw_speed, data.relative)

        pub.publish(para)

#calculating the time needed based on min speed of 50cm/s
def timecalc(distance, speed)
    #units:meters
    time = distance/speed
    return time

#starting the node
def start():

    global pub
    #publishing commands for auv to move
    pub = rospy.Publisher('Navikai/cmd', Twist)

    #start the node
    rospy.init node()
    rospy.spin()

if name == '__main__':
    start()
