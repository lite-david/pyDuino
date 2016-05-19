#Title: This is a Test designed to test workings of aw#
#Pranaydeep Singh#
#E-mail: theeviltwin@protonmail.com#
#Code for ar last changed: 18th May 2016#

import pyduino
ard = pyduino.arduino('/dev/ttyACM0',9600)
while(1):
    motorvalue=ard.ar(0)
    ledvalue=motorvalue/4
    ard.aw(3,ledvalue)