#!/usr/bin/python

import rospy
import random
from std_msgs.msg import Float64


def talker():
    pub2 = rospy.Publisher(
        '/calibrator/joint2_position_controller/command', Float64, queue_size=10)
    pub1 = rospy.Publisher(
        '/calibrator/joint1_position_controller/command', Float64, queue_size=10)
    pub0 = rospy.Publisher(
        '/calibrator/joint0_position_controller/command', Float64, queue_size=10)
    pub_fb = rospy.Publisher(
        '/calibrator/joint_forward_backward_position_controller/command', Float64, queue_size=10)
    pub_lr = rospy.Publisher(
        '/calibrator/joint_left_right_position_controller/command', Float64, queue_size=10)
    rospy.init_node('custom_talker', anonymous=True)
    r = rospy.Rate(1)  # 10hz

    msg0 = Float64() # -2.0 to 0.0
    msg1 = Float64() # -0.1 to 0.3
    msg2 = Float64() # -0.2 to 0.2
    msg_fb = Float64() # -1.0 to 1.0
    msg_lr = Float64() # -1.0 to 1.0

    while not rospy.is_shutdown():

        #for fb in range(-10,10):
        fb = random.randint(-10,10)
        msg_fb.data = -fb/10.0
        rospy.loginfo('setting fb {}'.format(msg_fb))
        pub_fb.publish(msg_fb)
        #for lr in range(-10,10):
        lr = random.randint(-10,10)
        msg_lr.data = -lr/10.0
        rospy.loginfo('setting lr {}'.format(msg_lr))
        pub_lr.publish(msg_lr)

        #for z in range(0,21):
        z = random.randint(0,21)
        msg0.data = -z/10.0
        rospy.loginfo('setting z {}'.format(msg0))
        pub0.publish(msg0)

        #for y in range(-1,3):
        y = random.randint(-1,3)
        msg2.data = y/10.0
        rospy.loginfo('setting y {}'.format(msg2))
        pub2.publish(msg2)

        # for x in range(-2,2):
        x = random.randint(-2,2)
        msg1.data = x/10.0
        rospy.loginfo('setting x {}'.format(msg1))
        pub1.publish(msg1)

        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
