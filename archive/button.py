#!/usr/bin/python
import RPi.GPIO as gpio

class Button(object):
	def __init__(self, pos_pin, neg_pin):
		self.pos_pin = pos_pin
		self.neg_pin = neg_pin

	def setup(self):
		gpio.setmode(gpio.BCM)
		gpio.setwarnings(True)
		gpio.setup(self.pos_pin, gpio.OUT)
		gpio.setup(self.neg_pin, gpio.IN)
		gpio.output(self.pos_pin, True)

	def press(self):
		return gpio.input(self.neg_pin)
