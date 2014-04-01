#!/usr/bin/python

import time
import RPi.GPIO as gpio

#Full Rotation: 200 steps @ 0.0005 second delay

cw = True
ccw = False

class Motor(object):
	def __init__(self, pin_step, pin_direction, rotation=cw):
		self.pin_step = pin_step
		self.pin_direction = pin_direction
		self.rotation = rotation
		self.min_delay = 0.0005

	def setup(self):
		gpio.setmode(gpio.BCM)
		gpio.setwarnings(True)

		gpio.setup(self.pin_step, gpio.OUT)
		gpio.setup(self.pin_direction, gpio.OUT)
		gpio.output(self.pin_direction, self.rotation)

	def set_rotation(self, rotation=cw):
		self.rotation = rotation
		gpio.output(self.pin_direction, self.rotation)

	def step(self, num_steps=200, speed=1):
		if speed > 1:
			print "Error: Loss of Motor Integrity"

		delay = (1/speed) * self.min_delay

		for i in range(0, num_steps+1):
			gpio.output(self.pin_step, True)
			time.sleep(delay)
			gpio.output(self.pin_step, False)
			time.sleep(delay)

	def rotate(self, num_rotations=1, speed=1):
		for i in range(0, num_rotations):
			self.step(speed=speed)
