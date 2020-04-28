#according to parameter thruster will move auv 50 cm/s

import rospy
import math

#following mission path on
#https://docs.google.com/presentation/d/1byiLI5PmSsF17uo3vu67g_D1zAS3xIYWgthhTiYyXOI/edit#slide=id.g6c44cb7098_37_23

from geomtry_msgs.msg import Twist

#calculating the time needed based on min speed of 50cm/s
def timecalc(distance, speed)
    #units:meters
    time = distance/speed
    return time

# Printing string command for simulator
def moving(data)
    twist = twist()

    #twist.mode = "guided"
    twist.x.translate = data.x
    twist.y.translate = data.y
    twist.z.translate = data.z
    twist.z.rotate = data.z_angular



# Opening gate code would go here

        #moving towards marker
        t = 0;
        time_move_to_marker  = timecalc(10,0.5)
        while t<time_move_to_marker:
            data.x = 0
            data.y = 0
            data.z = 1
            #update condition
            moving(data)
            t += 1

        t = 0
        time_to_uturn = 3.14
        while t< time_to_uturn:
            #data.xy.angular = math.cos(x)

            #moving in a semi-circle if AUV is 0.5m way from marker
            data.x = 0.5*math.cos(t)
            data.y = 0.5*math.sin(t)
            #data.xy.angular = 1;
            #update condition
            t += 0.1

        t = 0;
        time_move_to_marker  = timecalc(10,0.5)
        #returning back to gate from marker
        while t<time_move_to_marker:
            data.x = 0
            data.y = 0
            data.z = -1
            #update condition
            t += 1

#back at the gate

        # retuning to start point
        while t < time_move_to_gate:

            data.x = 0
            data.y = 0
            data.z = -1
            moving(data)
            #update condition
            t += 1



    pub.publish(twist)

#starting the node
def start():

    global pub
    #publishing commands for auv to move
    pub = rospy.Publisher('Navikai/cmd', Twist)

    #start the node
    rospy.init node()
    rospy.spin()
    
# mission script
#def main():
    while != rospy.is.shutdown:
        t = 0
        time_move_to_gate = timecalc(3, 0.5)
        # moving to
        while t < time_move_to_gate:

            data.x = 0
            data.y = 0
            data.z = 1
            moving(data)
            #update condition
            t += 1    

if name == '__main__':
    start()
