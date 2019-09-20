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
	


if __name__ == '__main__':
	
