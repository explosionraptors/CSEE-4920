#!/usr/bin/python

import RPi.GPIO as gpio
from motor import Motor
from rfid import Rfid
from database import Database
from time import sleep

# Database
host = 'localhost'

# Power
ON = True
OFF = False

# Entry
ADDRESS = 0
USERNAME = 1

if __name__ == '__main__':
	presses = 0

	motor = Motor(step_pin=23, dir_pin=24, power_pin=25)
	motor.setup()

	rfid = Rfid()
	rfid.setup()

	db = Database(host, "philosoraptor", "explosion", "doorman")
	db.setup()
	
	while True:
		addr = rfid.getaddr()
		if addr:
			print "Address: %s" % addr
			found, entry = db.checkaddr(addr)
			# Found is the number of entries that occur with address
			if found:
				user = entry[USERNAME]	# if found > 1, this may log incorrect user. shouldnt happen.
				motor.power(ON)
				motor.open()
				sleep(4)
				motor.close()
				motor.power(OFF)
			else:
				user = str()
			db.loguser(addr, user)
			addr = None	# should be unneccesary
	
	# Not gonna get here, but it's good practice
	db.close()

	"""while True:
		while True:
			addr = rfid.getaddr()
			print
			if addr:
				print "Output: %s\nTimes Scanned: %s" % (addr, presses)
				presses = 1
				found = db.checkaddr(addr)
				break
			sleep(0.1)
		if presses == 1:
			if found:
				motor.power(True)
				# motor.open(num_rotations=3, rotation_precision=100, speed=0.15)
				motor.open()
				# Do stuff here
				presses = 0
				addr = None
				sleep(2)
				# motor.close(num_rotations=3, rotation_precision=90, speed=1)
				motor.close()
				motor.power(False)"""
