import time
from datetime import datetime
from bh1750_smbus import BH1750
i = 0
sensor = BH1750()

file_name = "light_log.csv"

try:
    with open(file_name, "x") as f:
        f.write("time,lux\n")
except FileExistsError:
    pass

while i < 25:
    lux = sensor.read_lux()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = f"{now},{lux}\n"

    with open(file_name, "a") as f:
        f.write(line)

    print("Записано:", line.strip())
    time.sleep(1)
    i += 1