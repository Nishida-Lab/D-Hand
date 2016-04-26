# Author : Thibault Barbie

from driver import *
import time

b=DHand()
b.alarm_reset()

b.modbus_on()
b.servo_on()

# Should have a sleep if not it does not work
time.sleep(0.5)

i=0
while i<4:
    if(i%2==0):
        b.move_absolute_position(0.1,30,0.1,0.5)
    else:
        b.move_absolute_position(13,30,0.1,0.5)

    time.sleep(0.7)
    b.read_position()    
    i=i+1


while i<8:
    if(i%2==0):
        b.move_absolute_position(0.1,15,0.1,0.5)
    else:
        b.move_absolute_position(13,15,0.1,0.5)

    time.sleep(1.2)
    b.read_position()    
    i=i+1


time.sleep(1)

b.pause()

