from driver import *
import time

b=DHand()
b.alarm_reset()
b.modbus_on()
b.servo_on()
b.home_return()
b.start_off()
b.start_on()

time.sleep(0.500)

b.move_pos1()
b.start_off()
b.start_on()

print "Sleep"
time.sleep(3)
print "End of sleep"

b.move_pos2()
b.start_off()
b.start_on()

b.pause()
