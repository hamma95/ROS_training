#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import sys

key_mapping = { 'z': [ 0, 0.6], 'x': [0, -0.6],
				'q': [-0.6, 0], 'd': [0.6, 0],
				's': [ 0, 0] }
def keys_cb(msg, twist_pub):
	'''callback function for the keys topic.
	
	incoming keys are looked up in the dictionary. If a key is found,
        target velocities are extracted from the dictionary and published
        to the twist_pub topic.
        '''
	if len(msg.data) == 0 or msg.data[0] not in key_mapping:
		return # unknown key
	vels = key_mapping[msg.data[0]]
	t = Twist()
	t.angular.z = vels[0]
	t.linear.x = vels[1]
	twist_pub.publish(t)


if __name__ == '__main__':
	rospy.init_node('keys_to_twist')
	twist_pub = rospy.Publisher('key_vel', Twist, queue_size=1)
	rospy.Subscriber('keys', String, keys_cb, twist_pub)
	rospy.spin()
