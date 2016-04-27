# Author : Thibault Barbie

import minimalmodbus
import time


class DHand:

    def __init__(self,name,debug):
        minimalmodbus.BAUDRATE=38400

        self.s=minimalmodbus.Instrument("/dev/"+name,1)
        self.s.debug=debug

    def alarm_reset(self):
        # Alarm reset
        register=int('0407',16)
        self.s.write_bit(register,1,functioncode=5)
        
        # Restore normal status
        register=int('0407',16)
        self.s.write_bit(register,0,functioncode=5)
        
    def servo_on(self):
        # Servo ON
        register=int('0403',16)
        self.s.write_bit(register,1,functioncode=5)

    def servo_off(self):
        # Servo OFF
        register=int('0403',16)
        self.s.write_bit(register,0,functioncode=5)
        
    def modbus_on(self):
        # Modbus ON
        register=int('0427',16)
        self.s.write_bit(register,1,functioncode=5)

    def home_return(self):
        # Home return
        register=int('040B',16)
        self.s.write_bit(register,0,functioncode=5)
        self.s.write_bit(register,1,functioncode=5)
        
    def move_pos1(self):
        # Move to position 1
        register=int('9800',16)
        self.s.write_register(register,0001,functioncode=6)

    def move_pos2(self):
        # Move to position 2
        register=int('9800',16)
        self.s.write_register(register,0002,functioncode=6)

    def move_pos3(self):
        # Move to position 3
        register=int('9800',16)
        self.s.write_register(register,3,functioncode=6)

    def start_off(self):
        # Turn OFF the start signal
        register=int('0D00',16)
        self.s.write_register(register,4096,functioncode=6)

    def start_on(self):
        # Turn ON the start signal
        register=int('0D00',16)
        self.s.write_register(register,4104,functioncode=6)

    def pause(self):
        # Turn ON the pause
        register=int('0D00',16)
        self.s.write_register(register,16,functioncode=6)
        
    def ready(self):
        # Read if the servo is ready
        register=int('9005',16)
        print self.s.read_registers(register,1,functioncode=3)

    def move_absolute_position(self,position,speed,acceleration,push):
        # Move the servomotor to the position except if an obstacle is detected
        # position in mm, speed in mm/s, acceleration in G, push in percentage (0.2-0.7)
        register=39168 # In this function we should use dec and not hex
                
        if (position<0):
            position=0
        elif (position>13):
            position=13 # Maximum value before touching the palm
        if (speed<0):
            speed=0
        elif (speed>100):
            speed=100 # Maximum value (empirical)
        if (acceleration<0):
            acceleration=0
        elif (acceleration>0.209):
            acceleration=0.209 # Maximum value (empirical)
        if (push<0.2):
            push=0.2
        elif (push>0.7):
            push=0.7 # Maximum value said in manual
            
        l=[]
        l.append(0000)
        l.append(int(position*100))
        
        l.append(0000)
        l.append(10)

        l.append(0000)
        l.append(int(speed*100))
        
        l.append(int(acceleration*100))
        
        l.append(int(255*push))
        
        self.s.write_registers(register,l)

    def read_position(self):
        # Read the position of the servomotor
        register=int('9000',16)
        [a,b]= self.s.read_registers(register,2,functioncode=3)
        print b

    def read_alarm(self):
        # Read the position of the servomotor
        register=int('0500',16)
        print self.s.read_registers(register,6,functioncode=3)

    def read_position_completed(self):
        # Read the position of the servomotor
        register=int('9014',16)
        print self.s.read_registers(register,1,functioncode=3)

    def read_torque(self):
        # Read the position of the servomotor
        register=int('900C',16)
        print self.s.read_registers(register,2,functioncode=3)
            
