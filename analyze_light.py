import csv

file_name = "light_log.csv"

lux_values = []

with open(file_name, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        lux_values.append(float(row["lux"]))

print("How many dimensions:", len(lux_values))
print("Min:", min(lux_values))
print("Max:", max(lux_values))
print("Average value:", sum(lux_values) / len(lux_values))