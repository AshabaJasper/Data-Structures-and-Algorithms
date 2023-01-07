temperatures = [78.6, 80.1, 79.5, 82.4, 75.5, 73.6, 77.7, 79.6]

# let's say we want to calculate the average temperature
sum = 0
for temperature in temperatures:
  sum += temperature

average_temp = sum / len(temperatures)
print("Average temperature:", average_temp)


####### let's say we want to calculate the average temperature, but only for temperatures that are above 75 degrees
temperatures = [78.6, 80.1, 79.5, 82.4, 75.5, 73.6, 77.7, 79.6]

# let's say we want to calculate the average temperature, but only for temperatures that are above 75 degrees
sum = 0
num_temps_above_75 = 0
for temperature in temperatures:
  if temperature > 75:
    sum += temperature
    num_temps_above_75 += 1

# check if there were any temperatures above 75 degrees
if num_temps_above_75 > 0:
  average_temp = sum / num_temps_above_75
  print("Average temperature above 75 degrees:", average_temp)
else:
  print("No temperatures above 75 degrees.")
