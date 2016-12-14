#!/usr/bin/python


        #!/usr/bin/python

class arduino:


    def senddata(self,tosend):
        
        x = tosend%10
        y = (int)(tosend/10)%10
        z = (int)(tosend/100)
        data1 = str(x) + ":"
        data2 = str(y) + ":"
        data3 = str(z) + ":"

        self.ser.write(data1.encode('ascii'))
        self.ser.write(data2.encode('ascii'))
        self.ser.write(data3.encode('ascii'))
        
        

    def __init__(self,port,baud):
        import serial
        import time as t
        self.t = t
        global cw
        cw = 1
        print "Opening %s" %port
        self.ser = serial.Serial(port,baud)
        t.sleep(5)
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
            self.senddata(pm_cw_1)
            #flag = self.ser.write(chr(pm_cw_1))
            #return True if flag else False
        elif(mode == 'OUTPUT'):
            pm_cw_1 = cw  << 5 | pin | cw << 4
            self.senddata(pm_cw_1)
            #flag = self.ser.write(chr(pm_cw_1))
            #return True if flag else False

    def dw(self,pin,value):
            """
            Makes a specifed digital pin 'HIGH' or 'LOW'
            Useage: dw(pin,value)
            pin takes interger value from 0 to 13, value is 'HIGH' or 'LOW'5.
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
                
                self.senddata(dw_cw_2)
                #self.ser.write(chr(dw_cw_2))
                if value == 'HIGH':
                    a=dw_cw_1 | 15
                    self.senddata(a)
                    #self.ser.write(chr(dw_cw_1 | 15))
                    return True
                elif value == 'LOW':
                    self.senddata(dw_cw_1)
                    #self.ser.write(chr(dw_cw_1))
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
            """
            Changes the voltage of an analog Pin according to the value
            Useage: aw(pin,value)
            pin takes interger value from 0 to 13, value is between 0 and 255 only.
            """
            if(pin > 13 or pin < 0 or type(pin).__name__ != "int"):
                print "Error: Incorrect pin value"
                return False
            elif(value > 255 or value < 0 ):
                print "Error: Value can be between 255 and 0 only"
                return False
            aw_cw_1= cw << 6 | pin | cw << 4
            if self.ser.isOpen():
                self.senddata(aw_cw_1)
                self.senddata(value)
                #self.ser.write(chr(aw_cw_1))
                #self.ser.write(chr(value))
            else:
                print "Error: Could not open specified port"
                return False
    def ar(self,pin):
            """
            Reads specifed analog pin and prints its value on console between 0 and 1023.
            Usage: ar(pin)
            pin takes integer value from 0 to 13.
            """
            if(pin > 5 or pin < 0 or type(pin).__name__ != "int"):
                print "Error: Incorrect pin value"
                return False
            ar_cw_1 = cw << 6 | pin
            if self.ser.isOpen():
                self.senddata(ar_cw_1)
		senseval = self.ser.read()
		#self.ser.write(chr(ar_cw_1))
                #senseval = int(self.ser.readline())
                return senseval
            else:
                print "Error: Could not open specified port"
                return False
                    
        
    def delay(self,millisec):
        self.t.sleep(millisec/1000)
                
    
                    
