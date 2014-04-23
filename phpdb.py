#!/usr/bin/python

import requests

class Phpdb(object):
	def __init__(self):
		self.userlog = 'http://www.sensornetworks.engr.uga.edu/sp14/jyu/submituserlog.php'
		self.authkeys = 'http://www.sensornetworks.engr.uga.edu/sp14/jyu/viewAuth.php'

	def setup(self):
		pass

	def loguser(self, address):
		p = {'addr':address}
		r = requests.get(self.userlog, params=p)	
		if r.status_code != 200:
			print "Error: Could not log user"
			return False
		else:
			return True

	def checkaddr(self, address):
		r = requests.get(self.authkeys)
		if r.status_code != 200:
			print "Error: Could not access database"
			return None

		if address in r.json():
			return True
		else:
			return False
