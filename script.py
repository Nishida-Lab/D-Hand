# Author : Thibault Barbie

from driver import *
import time

b=Servo("ttyUSB0",False)
b.alarm_reset()

b.modbus_on()
b.servo_on()

# Should have a sleep if not it does not work
time.sleep(1.5)

i=0
while i<4:
    if(i%2==0):
        b.move_absolute_position(0.1,20,0.1,0.2)
    else:
        b.move_absolute_position(13,20,0.1,0.2)

    time.sleep(0.7)
    b.read_torque()    
    i=i+1


while i<10:
    if(i%2==0):
        b.move_absolute_position(0.1,10,0.1,0.2)
    else:
        b.move_absolute_position(13,10,0.1,0.2)

    time.sleep(1.2)
    b.read_torque()    
    i=i+1

print "Home return"
b.home_return()
time.sleep(3)

b.servo_off()

