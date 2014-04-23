#!/usr/bin/python

import MySQLdb

tables = dict(authkeys="(address TEXT, user TEXT)", userlog="(tdate DATE, ttime TIME, address TEXT, user TEXT)")

class Database(object):
	def __init__(self, host, username, password, rootdb):
		self.host = host
		self.username = username
		self.password = password
		self.rootdb = rootdb

	def setup(self):
		self.db = MySQLdb.connect(self.host, self.username, self.password, self.rootdb)
		self.curs = self.db.cursor()

	def loguser(self, address, user=str()):
		# address must exist as a string
		if type(address) != str or type(user) != str:
			print "Error: Invalid parameter types"
			return False

		try:
			self.curs.execute("insert into userlog values(CURRENT_DATE(), NOW(), '%s', '%s')" % (address, user))
			self.db.commit()
			return True # check call outputs
		except:
			print "Error logging user: %s with key: %s" % (user, address)
			self.db.rollback()
			return False

	def getdb(self, dbname='authkeys'):
		try:
			self.curs.execute("select * from %s" % dbname)
			db = self.curs.fetchall()
		except:
			print "Error fetching database: %s" % dbname
			db = tuple()
		return db

	def addaddr(self, address, user=str()):
		if type(address) != str or type(user) != str:
			print "Error: Invalid parameter type"
			return False
		try:
			self.curs.execute("insert into authkeys values('%s', '%s')" % (address, user))
			self.db.commit()
			return True # check call outputs
		except:
			print "Error logging user: %s with key: %s" % (user, address)
			self.db.rollback()
			return False
		

	def checkaddr(self, address):
		found = self.curs.execute("select * from authkeys where address='%s'" % address)
		entry = self.curs.fetchall()
		if found:
			entry = entry[0]
		return (found, entry)

	def cleardb(self, dbname):	# STUB
		fields = tables.get(dbname)
		if not fields:
			print "Error: Invalid database to clear"
			return
		self.curs.execute("drop table %s" % dbname)
		self.db.commit()
		self.curs.execute("create table %s %s" % (dbname, fields))
		self.db.commit()
		pass

	def close(self):
		self.db.close()
