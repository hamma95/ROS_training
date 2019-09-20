#!/usr/bin/env python3


''' we will output a Twist message every 100 milliseconds, or at a rate of 10 Hz,
    by simply repeating the last motion command if a new key was not pressed.
'''

# BEGIN ALL
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

key_mapping = { 'z': [ 0, 1], 'x': [0, -1], 
                'q': [-1, 0], 'd': [1,  0], 
                's': [ 0, 0] }
g_last_twist = None 

def keys_cb(msg, twist_pub):
  global g_last_twist
  if len(msg.data) == 0 or msg.data[0] not in key_mapping:
    return # unknown key.
  vels = key_mapping[msg.data[0]]
  g_last_twist.angular.z = vels[0]
  g_last_twist.linear.x  = vels[1]
  twist_pub.publish(g_last_twist)

if __name__ == '__main__':
  rospy.init_node('keys_to_twist')
  twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
  rospy.Subscriber('keys', String, keys_cb, twist_pub)
  # BEGIN RATE
  rate = rospy.Rate(10) #set rate to 10 Hz
  g_last_twist = Twist() # initializes to zero
  while not rospy.is_shutdown():
    twist_pub.publish(g_last_twist)
    rate.sleep() #this will ensure the loop runs exactly at 10 Hz 
  # END RATE
# END ALL
