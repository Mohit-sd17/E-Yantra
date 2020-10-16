#! /usr/bin/env python

# importing Required Libraries
import rospy
from geometry_msgs.msg import Twist


def main() :
    # Initializing node
    rospy.init_node( 'turtlesim_node', anonymous = True )
    
    # Storing initial Time in Seconds
    init_time = rospy.Time.now().to_sec()

    loop_rate = rospy.Rate( 2 )
    velocity_message = Twist()
    velocity_publisher = rospy.Publisher( '/turtle1/cmd_vel', Twist, queue_size = 10 )

    rospy.loginfo( 'Circular Motion of Turtle !! ' )

    # Setting the speed of message to move turtle in circular motion
    velocity_message.linear.x = 0.5
    velocity_message.angular.z = 0.5
    
    current_distance = 0 

    while current_distance < 6.5 :
        velocity_publisher.publish( velocity_message )
        loop_rate.sleep()

        current_time = rospy.Time.now().to_sec()
        current_distance = 0.5 * ( current_time - init_time )

        # Printing Result
        rospy.loginfo( 'Moving in a Circle' )
        rospy.loginfo( current_distance )
        rospy.loginfo( '\n' )
    
    loop_rate = rospy.Rate( 0.5 )
    rospy.loginfo( 'Goal Reached!!' )

    # Setting the speed of message to rotate turtle on its own axis 
    velocity_message.linear.x = 0
    velocity_message.angular.z = 1.5

    while True :
        velocity_publisher.publish( velocity_message )
        loop_rate.sleep()
        break
         

if __name__ == '__main__' :
    try :
        main()
    except rospy.ROSInterruptException:
        pass

