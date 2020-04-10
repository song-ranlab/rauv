This directory enables input from a controller and outputs data in ros sensor_msgs/Twist format.

Important: Must install joy node before using the code: http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick

Notes: 
  1. Change <indigo> to <melodic> in step 0.1.
  2. This was verified to work with a Razer Wolverine Ultimate controller. Should work for most linux-based controllers.
  3. after downloading joy node and teleop_test, begin with command "roslaunch teleop_test teleop.launch"
  4. If you see the error "[ERROR] [1586551123.346875896]: Couldn't open joystick force feedback!", it does not affect
     performance and can be ignored.
  5. Once nodes are running, view real-time output with command "rostopic echo /cmd_vel"
  6. Current mapping:
        x.translate: left joystick (up/down)
        y.translate: left joystick (left/right)
        z.translate: right joystick (up/down)
        z.rotate: right joystick (left/right)
  7. All output values range from -1 to +1. Next step will be scaling these values to be compatable with ardusub input.
