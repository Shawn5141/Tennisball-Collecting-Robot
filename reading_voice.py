#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from jsk_gui_msgs.msg import VoiceMessage
from std_msgs.msg import Bool
import numpy as np
from geometry_msgs.msg import Vector3
from sound_play.libsoundplay import SoundClient

class voice:
	_initiate='0'
	_small='0'
	_large='0'
	_stop='0'
	_data = Vector3()


	def voice_callback(self,data):
	#    rospy.loginfo("I heard %s",data.texts)
	    #print '\n-------------------'
	    for i in data.texts:
	        #print i
		sep = i.split(' ')
	        if 'catch' in sep:
	            print 'Start to catch'
	            self._initiate ='1'
		    self._small='0'
		    self._large='0'
		    self.soundhandle = SoundClient()
		    rospy.sleep(1)
		    self.soundhandle.say('yes my master.')
	            return
	
	        if 'one' in sep:
	            print 'easy as hell'
		    self._initiate ='1'
	            self._small='1'
		    self._large='0'
		    self.soundhandle = SoundClient()
		    rospy.sleep(1)
		    self.soundhandle.say('Yes my Lord. it is a piece of cake.')
		    
	    	    return

	        if 'two' in sep:
	            print 'it\n is\n big'
		    self._initiate = '1'
		    self._small = '0'
		    self._large ='1'     
		    self.soundhandle = SoundClient()
		    rospy.sleep(1)
		    self.soundhandle.say('Yes my Lord. Endless labor is my pleasure.')
	    	    return

	        if 'stop' in sep:
	            self._initiate ='0'
		    self._small='0'
		    self._large='0'
		    self.soundhandle = SoundClient()
		    rospy.sleep(1)
		    self.soundhandle.say('Thank you my master.     My torture has finally ended.')
	            print 'Thank\n you\n master'
	            return 

	def get_val(self):
		self._data.x=self._initiate
		self._data.y=self._small
		self._data.z=self._large
		return self._data.x, self._data.y, self._data.z

'''
if __name__ == '__main__':
	rospy.init_node('node_name')
	V=voice()
	rospy.Subscriber("/Tablet/voice", VoiceMessage, V.voice_callback)
	rospy.Subscriber("VoiceType", Vector3,V.get_val)
	

	#publish
	pub_value=rospy.Publisher("VocieType",Vector3,queue_size=1000)


	while not rospy.is_shutdown():
	    sleep_rate=rospy.Rate(10)
	    sleep_rate.sleep()
	    # spin() simply keeps python from exiting until this node is stopped
	    V._data.x, V._data.y, V._data.z = V.get_val()
	    pub_value.publish(V._data)
	    print V.get_val()
	    print "x,\t,y,\t,z", V._data.x, V._data.y, V._data.z
	    #rospy.spin()
'''