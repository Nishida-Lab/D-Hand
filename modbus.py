import minimalmodbus
import time
minimalmodbus.BAUDRATE=38400

s=minimalmodbus.Instrument('/dev/ttyUSB0',1)
s.debug=True

"""
# Alarm reset
register=int('0407',16)
s.write_bit(register,1,functioncode=5)

# Restore normal status
register=int('0407',16)
s.write_bit(register,0,functioncode=5)
"""




# Modbus ON
register=int('0427',16)
s.write_bit(register,1,functioncode=5)


# Servo ON
register=int('0D00',16)
s.write_register(register,4096,functioncode=6)

# Home return
register=int('0D00',16)
s.write_register(register,4112,functioncode=6)

time.sleep(0.500)

# Move to position 1
register=int('9800',16)
s.write_register(register,0002,functioncode=6)


#s.write_register(register,0001,functioncode=6)

# Turn OFF the start signal
register=int('0D00',16)
s.write_register(register,4096,functioncode=6)

# Turn ON the start signal
register=int('0D00',16)
s.write_register(register,4104,functioncode=6)

# Turn OFF the start signal
register=int('0D00',16)
s.write_register(register,4096,functioncode=6)


