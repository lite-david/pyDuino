#!/usr/bin/python

class arduino:

	def __init__(self,port,baud):
		import serial
		import time
		global cw
		cw = 1
		print "Opening %s" %port
		self.ser = serial.Serial(port,baud)
		if self.ser.isOpen():
			print "Opened %s at %d baud" % (port,baud)	
			return 
		else:
			print "Error: Could not open specified port"
			return 

	def pm(self,pin,mode):
		"""
		Sets specified arduino pin as input or output.
		Usage: pm(pin,mode)
		pin takes integer value from 0 to 13, mode is 'INPUT' or 'OUTPUT'

		"""
		if(pin > 13 or pin < 0 or type(pin).__name__ != "int"):
			print "Error: Incorrect pin value"
			return False
		elif(mode != 'OUTPUT' and mode != 'INPUT'):
			print "Error: Invalid mode"
			return False
		if(mode == 'INPUT'):	
			pm_cw_1 = cw  << 5 | pin 
			flag = self.ser.write(chr(pm_cw_1))
			return True if flag else False
		elif(mode == 'OUTPUT'):
			pm_cw_1 = cw  << 5 | pin | cw << 4
			flag = self.ser.write(chr(pm_cw_1))
			return True if flag else False

	def dw(self,pin,value):
		"""
		Makes a specifed digital pin 'HIGH' or 'LOW'
		Useage: dw(pin,value)
		pin takes interger value from 0 to 13, value is 'HIGH' or 'LOW'

		"""
		if(pin > 13 or pin < 0 or type(pin).__name__ != "int"):
			print "Error: Incorrect pin value"
			return False 
		elif(value is not "HIGH"):
			if(value is not "LOW"):
				print "Error: Value can be either HIGH or LOW"
				return False
		dw_cw_1 = cw << 6 | cw << 5 | cw << 4
		dw_cw_2 = dw_cw_1 | pin
		if self.ser.isOpen():
			self.ser.write(chr(dw_cw_2))
			if value == 'HIGH':
				self.ser.write(chr(dw_cw_1 | 15))
				return True
			elif value == 'LOW':
				self.ser.write(chr(dw_cw_1))
				return True
		else:
			print "Error: Could not open specified port"
			return False

	def dr(self,pin):
		"""
		Reads specifed digital pin and prints its value on console
		Useage: dr(pin)
		pin takes integer value from 0 to 13.

		"""
		if(pin > 13 or pin < 0 or type(pin).__name__ != "int"):
			print "Error: Incorrect pin value"
			return False
		dr_cw_1 = cw << 6 | cw << 5 | pin
		if self.ser.isOpen():
			self.ser.write(chr(dr_cw_1))
			return self.ser.read()
		else:
			print "Error: Could not open specified port"
			return False
                    
	def aw(self,pin,value):
		if(pin > 13 or pin < 0 or type(pin).__name__ != "int"):
			print "Error: Incorrect pin value"
			return False
        	elif(value > 255 or value < 0 ):
			print "Error: Value can be between 255 and 0 only"
			return False
		aw_cw_1= cw << 6 | pin | cw << 4
		if self.ser.isOpen():
			self.ser.write(chr(aw_cw_1))
			self.ser.write(chr(value))
		else:
			print "Error: Could not open specified port"
			return False
	def ar(self,pin):
		if(pin > 5 or pin < 0 or type(pin).__name__ != "int"):
			print "Error: Incorrect pin value"
			return False
		ar_cw_1 = cw << 6 | pin
		if self.ser.isOpen():
			self.ser.write(chr(ar_cw_1))
			senseval = int(self.ser.readline())
			return senseval
		else:
			print "Error: Could not open specified port"
			return False
		        
	    

	def delay(millisec):
		time.sleep(millisec/1000)

