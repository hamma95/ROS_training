#!/usr/bin/env python3


''' we will output a Twist message every 100 milliseconds, or at a rate of 10 Hz,
    by simply repeating the last motion command if a new key was not pressed.
'''


import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

key_mapping = { 'z': [ 0, 1], 'x': [0, -1], 
                'q': [-1, 0], 'd': [1,  0], 
                's': [ 0, 0] }
 

def keys_cb(msg, twist_pub):
  

if __name__ == '__main__':
  
