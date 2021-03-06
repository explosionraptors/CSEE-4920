#!/usr/bin/python

import serial

class Rfid(object):
	def __init__(self):
		# set variables [wut variables]
		pass

	def setup(self):
		# setup serial
		loop = True
		tries = 0
		while loop:
			try:
				self.rfid = serial.Serial('/dev/ttyAMA0', 9600)
				loop = False
			except OSError:
				tries += 1
				print "OSError: while setting up RFID\nTry %s of 5..." % tries
				if tries > 5:
					print "Cannot setup RFID. Check hardware configuration... exiting"
					exit(1)
				else:
					loop = True
	
	def __addrparse(self, addr):
		temp = addr.rstrip()
		idx = temp.find('\x02') + 1
		if idx == 0:
			print "Error: issue finding start of address"

		addrchk = temp[idx:]
		alen = len(addrchk)
		if alen == 12:
			address = addrchk[0:10]
			checksum = addrchk[10:12]
		else:
			print "Error: We have an issue that needs immediate fixing"

		return address, checksum

	def getaddr(self):
		line = self.rfid.readline()
		addr, chk = self.__addrparse(line)
		# calculate checksum and verify integrity
		return addr
