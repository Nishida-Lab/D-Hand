from driver import *
import time

b=DHand()
b.alarm_reset()
b.modbus_on()
b.servo_on()
#b.home_return()
#b.start_off()
#b.start_on()

time.sleep(0.5)

i=0
while i<10:
    if(i%2==0):
        b.move_pos1()
    else:
        b.move_pos2()
    b.start_off()
    b.start_on()

    print "Sleep"
    time.sleep(1)
    print "End of sleep"
        
    i=i+1

b.pause()
