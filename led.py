#!/usr/bin/python

import RPi.GPIO as gpio
from time import sleep

# States
ERR=-1
OFF=0
RED=1
GREEN=2
BOTH=3

class Led(object):
	def __init__(self, red_pin=4, green_pin=17):
		self.red_pin = red_pin
		self.green_pin = green_pin
		self.ERR = ERR
		self.OFF = OFF
		self.RED = RED
		self.GREEN = GREEN
		self.BOTH = BOTH

	def setup(self):
		gpio.setmode(gpio.BCM)
		gpio.setwarnings(False)
		gpio.setup(self.red_pin, gpio.OUT)
		gpio.setup(self.green_pin, gpio.OUT)

	def setstate(self, state=OFF):
		if state == ERR:
			while True:
				gpio.output(self.red_pin, True)
				gpio.output(self.green_pin, False)
				sleep(0.1)
				gpio.output(self.green_pin, True)
				gpio.output(self.red_pin, False)
				sleep(0.1)
		elif state == OFF:
			gpio.output(self.red_pin, False)
			gpio.output(self.green_pin, False)
		elif state == RED:
			gpio.output(self.red_pin, True)
			gpio.output(self.green_pin, False)
		elif state == GREEN:
			gpio.output(self.red_pin, False)
			gpio.output(self.green_pin, True)
		elif state == BOTH:
			gpio.output(self.red_pin, True)
			gpio.output(self.green_pin, True)
		else:
			print "Error: LED State should never end up here"
