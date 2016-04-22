import minimalmodbus
import time


class DHand:

    def __init__(self):
        minimalmodbus.BAUDRATE=38400

        self.s=minimalmodbus.Instrument('/dev/ttyUSB0',1)
        self.s.debug=False

    def alarm_reset(self):
        # Alarm reset
        register=int('0407',16)
        self.s.write_bit(register,1,functioncode=5)
        
        # Restore normal status
        register=int('0407',16)
        self.s.write_bit(register,0,functioncode=5)
        
    def servo_on(self):
        # Servo ON
        register=int('0D00',16)
        self.s.write_register(register,4096,functioncode=6)

    def modbus_on(self):
        # Modbus ON
        register=int('0427',16)
        self.s.write_bit(register,1,functioncode=5)
        
    def home_return(self):
        # Home return
        self.s.debug=True
        register=int('0D00',16)
        self.s.write_register(register,4112,functioncode=6)
        self.s.debug=False

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
        
        
        
