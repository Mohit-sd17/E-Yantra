#!/usr/bin/python
# -*- coding: utf-8 -*-

# importing Required Libraries
import math
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

theta = 0

# Python Main
if __name__ == '__main__':
    try:
        circular_motion()
    except rospy.ROSInterruptException:
        pass


# circular_motion Function
def circular_motion() :

    # Initializing node to sub msg theta from Pose and pub response to Twist
    rospy.init_node( 'circular_motion', anonymous=True )

    # Defining Twist() as velocity_message
    velocity_message = Twist()

    # Defining Publisher of topic /turtle1/cmd_vel as velocity_publisher
    velocity_publisher = rospy.Publisher( '/turtle1/cmd_vel', Twist, queue_size=10 )

    # Subscribing the data from topic /turtle1/pose
    rospy.Subscriber( '/turtle1/pose', Pose, poseCallback )

    rospy.loginfo( ' Circular Motion of Turtle !! ' )

    # declaring the linear_speed
    velocity_message.linear.x = 1

    # defining the angular speed using formula
    # angular_speed = linear_speed / radius for circular motion
    # For turtlesim the range of radius is [ 0 - 2.5 ]
    velocity_message.angular.z = 1

    # initializing current distance travelled by turtle
    current_distance = 0.0

    # calculating the final distance travelled by turtle for 1 complete circle
    final_distance = 2 * math.pi

    # initializing flag for more accurate result
    flag = 0

    while current_distance < final_distance:

        # publishing current_velocity message to topic /turtle1/cmd_vel
        velocity_publisher.publish(velocity_message)

        # condition to complete Semi-Circle and using flag to avoid repetation
        if theta >= 0 and flag == 0:

            # calculating the distance_travelled using formula theta * radius
            current_distance = theta
        else:

            # calculating the distance_travelled using formula
            # final_distance + theta * radius
            current_distance = final_distance + theta

            # changing the value of flag to avoid the repetition of if
            flag = 1

        # Printing Result
        rospy.loginfo( 'Moving in a Circle\n' + str( current_distance ) + '\n' )

        rospy.loginfo( 'Goal Reached' )

    # Setting the speed of message to rotate turtle on its own axis
    # by changing value of linear_speed of turtle to 0
    velocity_message.linear.x = 0

    # changing the angular speed for better result  i.e it is manditory
    velocity_message.angular.z = 1.5

    # For making the turtle point perfect 90 specifying angle
    final_angle = math.pi * theta

    while theta < final_angle:
        velocity_publisher.publish( velocity_message )


# function  to Stores the theta message
# subscribing from /turtle1/pose in global variable theta
def poseCallback( pose_message ) :
    global theta
    theta = pose_message.theta
