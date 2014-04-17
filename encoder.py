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
		
		gpio.setup(gpio.clk_pin, gpio.IN, pull_up_down=gppio.PUD_DOWN)
		gpio.setup(gpio.dir_pin, gpio.IN, pull_up_down=gppio.PUD_DOWN)
		
		gpio.add_event_detect(self.clk_pin, gpio.RISING, call_back=self.__pulse)
		
	def __pulse(self, channel):
		self.pulses += 1
		
	def getpulses(self):
		return self.pulses