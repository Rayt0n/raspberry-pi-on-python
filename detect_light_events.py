import csv

file_name = "light_log.csv"
state = "off"
infelicity = 50   
lux_values = []
time_values = []

with open(file_name, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        lux_values.append(float(row["lux"]))
        time_values.append((row["time"]))

events = []
time_of_events = []

for i in range(1, len(lux_values)):
    prev = lux_values[i-1]
    curr = lux_values[i]
    delta = prev - curr
    if delta < 0:
        delta = delta * -1

    if delta >= infelicity and state == "off":
        events.append(f"Light on")
        time_of_events.append(time_values[i])
        state = "on"

    elif delta >= infelicity and state == "on":
        events.append(f"Light off")
        time_of_events.append(time_values[i])
        state = "off"

for i in range(1, len(events)):
    print(f"{events[i]} in time: {time_of_events[i]}")