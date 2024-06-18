/*Create a small turtle speed publisher*/

#include <ros/ros.h>

#include <geometry_msgs/Twist.h>

int main(int argc, char **argv)

{

    ros::init(argc, argv, "turtle_velocity_publisher");//ROS node initialization

    ros::NodeHandle n;//Here is create handle

    //Create a Publisher, publish a topic named /turtle1/cmd_vel, the message type is geometry_msgs::Twist, and the queue length is 10

    ros::Publisher turtle_vel_pub = n.advertise<geometry_msgs::Twist>

    ("/turtle1/cmd_vel", 10);

    ros::Rate loop_rate(10);//Set the frequency of the loop

    while (ros::ok())

    {

        //Initialize the message to be published, the type must be consistent with Publisher

        geometry_msgs::Twist turtle_vel_msg;

        turtle_vel_msg.linear.x = 0.8;

        turtle_vel_msg.angular.z = 0.6;

        turtle_vel_pub.publish(turtle_vel_msg);// Publish speed news

        //Print published speed content

        ROS_INFO("Publsh turtle velocity command[%0.2f m/s, %0.2f rad/s]",

        turtle_vel_msg.linear.x, turtle_vel_msg.angular.z);

        loop_rate.sleep();//Delay according to cycle frequency

    }

    return 0;

}
