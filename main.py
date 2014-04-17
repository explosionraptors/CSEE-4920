#!/usr/bin/python

import RPi.GPIO as gpio
from motor import Motor
from rfid import Rfid
from database import Database
from led import Led
from encoder import Encoder
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
    # Components
	ld = Led(red_pin=4, green_pin=17)
	ld.setup()
    
    motor = Motor(step_pin=23, dir_pin=24, power_pin=25)
	motor.setup()

    encoder = Encoder(clk_pin=22, dir_pin=27)
    encoder.setup()

	db = Database(host, "philosoraptor", "explosion", "doorman")
	db.setup()

	rfid = Rfid()
	rfid.setup()

    # Main Loop
	while True:
		ld.setstate(ld.BOTH)
		addr = rfid.getaddr()
		if addr:
			#print "Address: %s" % addr
			found, entry = db.checkaddr(addr)
			# Found is the number of entries that occur with address
			if found:
				ld.setstate(ld.GREEN)
				user = entry[USERNAME]	# if found > 1, this may log incorrect user. shouldnt happen.
				motor.power(ON)
                # Hardcoded
                # motor.open()
                
                turning = True
                while turning:
                    p0 = encoder.getpulses()
                    motor.rotate(num_steps=50, speed=0.2)
                    motor.steps += 50
                    p1 = encoder.getpulses()
                    if (p1 - p0) < # clk pulses equivalent to 50 steps
                        turning = False
                
				sleep(4)    # delay between release
                
                steps = motor.steps - 50    # always release less than we take
                motor.close(num_rotations=1, rotation_precision=steps)
				motor.power(OFF)
			else:
				ld.setstate(ld.RED)
				user = str()
				sleep(2)	# make illegal user wait
			db.loguser(addr, user)
			addr = None	# should be unneccesary
	
	# Not gonna get here, but it's good practice
	db.close()
	ld.setstate(ld.OFF)
