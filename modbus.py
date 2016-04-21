import minimalmodbus

minimalmodbus.BAUDRATE=38400

s=minimalmodbus.Instrument('/dev/ttyUSB0',1)

register=int('0D03',16)
#print s.read_registers(register,1)
s.debug=True
s.write_register(register,0002,functioncode=6)
register=int('0D00',16)
s.write_register(register,4096,functioncode=6)
s.write_register(register,4104,functioncode=6)


#print s.read_register(register)
