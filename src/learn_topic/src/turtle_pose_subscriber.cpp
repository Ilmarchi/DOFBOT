/*Create a small turtle to receive the current pose information*/

#include <ros/ros.h>

#include "turtlesim/Pose.h"

// After receiving the message, you will enter the message callback function, which will process the received data.

void turtle_poseCallback(const turtlesim::Pose::ConstPtr& msg)

{

    // Print received messages

    ROS_INFO("Turtle pose: x:%0.3f, y:%0.3f", msg->x, msg->y);

}

int main(int argc, char **argv)

{

    ros::init(argc, argv, "turtle_pose_subscriber");// Initialize ROS node

    ros::NodeHandle n;//Here is create handle

    // Create a subscriber. The topic of subscription is the topic of /turtle1/pose. poseCallback is the callback function.

    ros::Subscriber pose_sub = n.subscribe("/turtle1/pose", 10,turtle_poseCallback);

    ros::spin(); // Loop waiting for callback function

    return 0;

}
