#according to parameter thruster will move auv 50 cm/s

import rospy
import math


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

        t = 0;
        time_move_to_marker  = (10,0.5)
        while t<time_move_to_marker:
            data.x = 0;
            data.y = 1;
            data.z = 0;


        while t< time_to_uturn:
            #data.xy.angular = math.cos(x)
            data.xy.angular = 1;


#printing string command for simulator
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

def timecalc(distance, speed)
    #units:meters
    time = distance/speed
    return time
