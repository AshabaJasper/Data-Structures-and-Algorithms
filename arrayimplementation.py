temperatures = [78.6, 80.1, 79.5, 82.4, 75.5, 73.6, 77.7, 79.6]

# let's say we want to calculate the average temperature
sum = 0
for temperature in temperatures:
  sum += temperature

average_temp = sum / len(temperatures)
print("Average temperature:", average_temp)
