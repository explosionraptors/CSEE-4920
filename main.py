#!/usr/bin/python

import RPi.GPIO as gpio
from motor import Motor
from rfid import Rfid
from phpdb import Phpdb
from database import Database
from led import Led
from encoder import Encoder
from time import sleep

# Power
ON = True
OFF = False

# Entry
ADDRESS = 0
USERNAME = 1

if __name__ == '__main__':
    	# Components
	ld = Led(red_pin=4, green_pin=17)
	ld.setup()
    
	motor = Motor(step_pin=23, dir_pin=24, power_pin=18)
	motor.setup()

	encoder = Encoder(clk_pin=22, dir_pin=27)
	encoder.setup()

	pdb = Phpdb()
	pdb.setup()	# Pass

	# LocalDB
	db = Database('localhost', 'philosoraptor', 'explosion', 'doorman')
	db.setup()

	rfid = Rfid()
	rfid.setup()

	# Main Loop
	while True:
		ld.setstate(ld.BOTH)
		addr = rfid.getaddr()
	
		if addr:
			print "Address: %s" % addr
			try:	# in the event of a failure (no connection)	
				found, authkeys = pdb.checkaddr(addr)
			except:	# default to local database
				found, toss = db.checkaddr(addr)
				authkeys = None

			# Update local
			if authkeys:
				db.cleardb('authkeys')
				for k in authkeys:
					db.addaddr(str(k))	# cast from unicode to string

			if found != 0 and found != None:
				ld.setstate(ld.GREEN)
				motor.power(ON)
                					
				motor.open(num_rotations=1, rotation_precision=10)
                		turning = True
                		d = gpio.input(encoder.dir_pin)
                    		while turning:
					motor.open(num_rotations=1, rotation_precision=10, speed=0.25)
                    			if d != gpio.input(encoder.dir_pin):	# Will sense slippage
						print "Change in direction"
						turning = False
					elif motor.steps > 2000:		# Hardcoded Max Steps
						print "Reached 2000 steps"
						turning = False
				sleep(5)    # delay between release
				motor.power(OFF)
		    	else:
				ld.setstate(ld.RED)
				sleep(2)	# make illegal user wait
			try:		    	
				pdb.loguser(addr)
			except:
				db.loguser(addr)
			addr = None	# should be unneccesary
			found = None
	
	db.close()
	ld.setstate(ld.OFF)
