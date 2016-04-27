# Author : Thibault Barbie

# This file initialise the servomotor. It removes the alarm and do a home return.

from driver import *
import time

b=Servo("ttyUSB0",False)

b.alarm_reset()
print "Alarm"
time.sleep(1.5)

b.modbus_on()
print "Modbus on"
time.sleep(1.5)

b.servo_on()
print "Servo On"
time.sleep(1.5)

b.home_return()
print "Home"
time.sleep(1.5)

b.servo_off()
print "Servo Off"
