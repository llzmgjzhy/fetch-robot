#!/usr/bin/python
import rospy
import navigation2 as nv2
from geometry_msgs.msg import Twist
from std_msgs.msg import String


class Voice_Control(object):

    def __init__(self):

        self.speed = 0.2
        self.msg = Twist()

        rospy.init_node("asr_control",'navtopoint')
        rospy.on_shutdown(self.shutdown)

        self.pub_ = rospy.Publisher("mobile_base/commands/velocity", Twist, queue_size=10)

        rospy.Subscriber("kws_data", String, self.parse_asr_result)
        rospy.spin()

    def parse_asr_result(self, detected_words):
        """Function to perform action on detected word"""
        if detected_words.data.find("full speed") > -1:
            if self.speed == 0.2:
                self.msg.linear.x = self.msg.linear.x * 2
                self.msg.angular.z = self.msg.angular.z * 2
                self.speed = 0.4
                print('full speed')
        elif detected_words.data.find("half speed") > -1:
            if self.speed == 0.4:
                self.msg.linear.x = self.msg.linear.x / 2
                self.msg.angular.z = self.msg.angular.z / 2
                self.speed = 0.2
                print('half speed')
        elif detected_words.data.find("forward") > -1:
            self.msg.linear.x = self.speed
            self.msg.angular.z = 0
            print('forward')
        elif detected_words.data.find("move") > -1:
            print('move')
            nv2.main(2.95,3.3,0)
            # if self.msg.linear.x != 0:
            #     if self.msg.angular.z < self.speed:
            #         self.msg.angular.z += 0.5
            #         self.msg.linear.x = 0
            # else:
            #     self.msg.angular.z = self.speed * 2
        elif detected_words.data.find("right") > -1:
            print('right')
            if self.msg.linear.x != 0:
                if self.msg.angular.z > -self.speed:
                    self.msg.angular.z -= 0.5
                    self.msg.linear.x = 0
            else:
                self.msg.angular.z = -self.speed * 2
        elif detected_words.data.find("back") > -1:
            self.msg.linear.x = -self.speed
            self.msg.angular.z = 0
            print('back')
        elif detected_words.data.find("stop") > -1 or detected_words.data.find("halt") > -1:
            self.msg = Twist()

        self.pub_.publish(self.msg)

    def shutdown(self):
        rospy.loginfo("Stop ASRControl")
        self.pub_.publish(Twist())
        rospy.sleep(1)


if __name__ == "__main__":
    Voice_Control()
