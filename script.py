from driver import *
import time

b=DHand()
b.alarm_reset()

b.modbus_on()
b.servo_on()

time.sleep(0.5)

i=0
while i<6:
    if(i%2==0):
        b.move_absolute_position(0,40)
    else:
        b.move_absolute_position(13,40)

    time.sleep(0.7)
        
    i=i+1


while i<10:
    if(i%2==0):
        b.move_absolute_position(0,15)
    else:
        b.move_absolute_position(13,15)

    time.sleep(1.2)
        
    i=i+1
    
time.sleep(1)


b.pause()
