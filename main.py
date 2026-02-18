from time import sleep
from RPLCD.i2c import CharLCD
from bh1750_smbus import BH1750

sensor = BH1750()
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

state = "off"
last_lux = None

while True:
    lux = sensor.read_lux()

    if last_lux is None:
        last_lux = lux

    if lux > 50 and state == "off":
        state = "on"

    if lux < 30 and state == "on":
        state = "off"

    lcd.clear()
    lcd.write_string(f"Light: {state}")
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"Lux: {int(lux)}")

    last_lux = lux
    sleep(1)