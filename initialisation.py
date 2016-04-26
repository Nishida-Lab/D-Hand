# Author : Thibault Barbie

# This file initialise D-Hand. It removes the alarm and do a home return.

from driver import *
import time

b=DHand()

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

b.pause()
print "Pause"
