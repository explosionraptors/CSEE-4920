#!/usr/bin/python

import time
import RPi.GPIO as gpio

# Fastest Full Rotation : 200 steps @ 0.0005 second delay

# Enum
FULL = 200	# steps
HALF = FULL / 2
QUARTER = HALF / 2
EIGHTH = QUARTER / 2

CW = True
CCW = False

class Motor(object):
	def __init__(self, step_pin, dir_pin, rotation=CW):
		self.step_pin = step_pin
		self.dir_pin = dir_pin
		self.rotation = rotation
		self.min_delay = 0.0005

	def setup(self):
		gpio.setmode(gpio.BCM)
		gpio.setwarnings(True)

		gpio.setup(self.step_pin, gpio.OUT)
		gpio.setup(self.dir_pin, gpio.OUT)
		gpio.output(self.dir_pin, self.rotation)

	def set_rotation(self, rotation=CW):
		self.rotation = rotation
		gpio.output(self.dir_pin, self.rotation)

	def step(self):
		gpio.output(self.step_pin, True)
		time.sleep(self.min_delay)
		gpio.output(self.step_pin, False)
		
	def rotate(self, num_steps=FULL, speed=1):
		if speed > 1:
			print "Error: Loss of Motor Integrity"

		delay = (1/speed) * self.min_delay
		for i in range(0, num_steps):
			self.step()
			time.sleep(delay)

	def open(self, num_rotations=1, rotation_precision=FULL, speed=1):
		for i in range(0, num_rotations):
			self.rotate(num_steps=rotation_precision, speed=speed)
