#!/usr/bin/python

import RPi.GPIO as gpio
from motor import Motor
from button import Button
import serial
from time import sleep

whitelist = ['4800E534D7']

def process_output(output):
	output_split = output.split()
	addr_list = output_split[2:7]
	addr = "".join(addr_list)
	return addr

if __name__ == '__main__':
	presses = 0

	motor = Motor(step_pin=23, dir_pin=24)
	#button = Button(pos_pin=17, neg_pin=22)

	motor.setup()
	#button.setup()
	rfid = serial.Serial('/dev/ttyACM0', 9600)

	while True:
		while True:
			rfid_output = rfid.readline()
			if rfid_output:
				print "Output: %s\nTimes Scanned: %s" % (rfid_output, presses)
				presses = 1
				break
			sleep(0.1)
		if presses == 1:
			addr = process_output(rfid_output)
			if addr in whitelist:
				motor.set_rotation(True)
				motor.open(num_rotations=3, rotation_precision=100, speed=0.15)
				# Do stuff here
				presses = 0
				rfid_output = None
				motor.set_rotation(False)
				sleep(8)
				motor.open(num_rotations=3, rotation_precision=90, speed=1)





		#if button.press() == True:
		#	presses += 1
		#	if count == 1:
		#		motor.step()
		#else:
		#	count = 0
