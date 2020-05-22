#!/usr/bin/python

import rospy
from std_msgs.msg import Float64


def talker():
    pub = rospy.Publisher(
        '/calibrator/joint2_position_controller/command', Float64)
    pub2 = rospy.Publisher(
        '/calibrator/joint1_position_controller/command', Float64)
    rospy.init_node('custom_talker', anonymous=True)
    r = rospy.Rate(10)  # 10hz

    msg = Float64()
    msg2 = Float64()
    i = 0
    while not rospy.is_shutdown():
        msg.data = i * 2*3.141/60.0
        msg2.data = i * 2*3.141/60.0
        rospy.loginfo(msg)
        pub.publish(msg)
        pub2.publish(msg2)
        r.sleep()
        i += 1


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
