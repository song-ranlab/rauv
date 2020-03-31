//Based off the ros wiki with placehoder for nodes
//working on python version right now

#include <ros/ros.h> //What are we publishing to 

//express velocity in free space in linear and angular form/ 
#include <geometry_msgs/Twist.h> 

//What we are listening to
//need to do this on computer: http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick 
#include <sensor_msgs/Joy.h>

class TeleopNavi
{
public:
  TeleopNavi(); // public things can be changed in the man

private:
  void joyCallback(const sensor_msgs::Joy::ConstPtr& joy); // private functions can’t be changed in main

  ros::NodeHandle nh;

  int linear, angular;
  double l_scale, a_scale;
  
  ros::publisher vel_pub//publish as cmd_vel;
  ros::subscriber joy_sub //input from controller;

};


TeleopNavi::TeleopNavi():
  linear(1),
  angular(2)
{

  nh_.param("axis_linear", linear, linear);
  nh_.param("axis_angular", angular, angular);
  nh_.param("scale_angular", a_scale, a_scale);
  nh_.param("scale_linear", l_scale, l_scale);


  vel_pub_ = nh_.advertise<geometry_msgs::Twist>("NaviKai/cmd_vel", 1);

//if processing t0o slow change the number 10
  joy_sub = nh_.subscribe<sensor_msgs::Joy>("joy", 10, &Teleop::joyCallback, this);

}

void TeleopTurtle::joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
  geometry_msgs::Twist twist;
  twist.angular.z = a_scale*joy->axes[angular];
  twist.linear.x = l_scale*joy->axes[linear];
  vel_pub.publish(twist);
}


int main(int argc, char** argv)
{
  ros::init(argc, argv, "teleop");
  Teleop teleop;

  print(“hey this works”);

  ros::spin();
}
