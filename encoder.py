#!/usr/bin/python

import RPi.GPIO as gpio

class Encoder(object):
	def __init__(self, clk_pin, dir_pin):
		self.pulses = 0
		self.clk_pin = clk_pin
		self.dir_pin = dir_pin
				

	def setup(self):
		gpio.setmode(gpio.BCM)
		gpio.setwarnings(False)
		
		gpio.setup(self.clk_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
		gpio.setup(self.dir_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
		
		gpio.add_event_detect(self.clk_pin, gpio.RISING, callback=self.__pulse)
		#gpio.add_event_detect(self.dir_pin, gpio.BOTH)		

	def __pulse(self, channel):
		if gpio.input(self.dir_pin):
			self.pulses += 1
		else:
			self.pulses -= 1

	#def setslip(self):
		#self.
		#if gpio.event_detected(self.dir_pin):
				

	#def checkslip(self):
		

	def getpulses(self):
		return self.pulses
