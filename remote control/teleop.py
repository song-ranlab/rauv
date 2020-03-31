import rospy
from std_msgs.msg import string

# grabing input from user
'''
need to instal joy on computer: http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick#Installing
'''
'''
intended for xbox controller
'''

from sensor_msgs.msg Joy
from geomtry_msgs.msg import


def callback(data)
    twist = Twist()

    #verticle of left stick
    #move foward or backwards
    twist.linear_y = data.axes[1] 
    #horizontal of left stick
    #move left right
    twist.linear_x = data.axes[0]

    #move up or down
    # 4 = left button, 5 = right button
    twist.linear_z_u = data.buttons[4]
    twist.linear_z_d = data.buttons[5]

    #rotate on x - y plane
    #horizontal of the right stick
    twist.angular_xy = data.axes[2]

    #rotate y-z axis
    #verticle of the right stick
    twist.angularr_yz = data.axes[3]
    pub.publish(twist)


def start():

    global pub
    #publishing commands for auv to move
    pub = rospy.Publisher('Navikai/cmd', Twist)

    # subscribed for user input
    rospy.Subscriber("joy", Joy, callback)

    #start the node
    rospy.init node()
    rospy.spin()

if name == '__main__':
    start()
