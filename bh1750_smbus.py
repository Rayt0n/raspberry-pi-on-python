from smbus2 import SMBus
import time
class BH1750:
	def __init__(self,bus_number=1,addr=0x23):
		self.bus = SMBus(bus_number)
		self.addr = addr
		self.POWER_ON = 0x01
		self.RESET = 0x07
		self.CONT_HIRES_MODE = 0x10
		self.bus.write_byte(self.addr, self.POWER_ON)
		time.sleep(0.1)
		self.bus.write_byte(self.addr, self.RESET)
		time.sleep(0.1)

	def read_lux(self):
		self.bus.write_byte(self.addr,self.CONT_HIRES_MODE)
		time.sleep(0.2)
		data = self.bus.read_i2c_block_data(self.addr, self.CONT_HIRES_MODE, 2)
		lux = (data[0] << 8 | data[1]) / 1.2
		return lux 
