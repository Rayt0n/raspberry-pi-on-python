from RPLCD.i2c import CharLCD
from time import sleep
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)
lcd.backlight_enabled = True
lcd.write_string("Smart Room")
lcd.cursor_pos = (1,0)
lcd.write_string("System OK")
sleep(10)
lcd.clear()