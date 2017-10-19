temperature_1 = int (input("Input the first temperature"))
temperature_2 = int (input("Input the second temperature"))
temperature_3 = int (input("Input the third temperature"))
temperature_4 = int (input("Input the fourth temperature"))

total_temperature = temperature_1 + temperature_2 + temperature_3 + temperature_4
average_temperature = total_temperature / 4

print(average_temperature)
temp_list = [temperature_1, temperature_2, temperature_3, temperature_4]
print(max(temp_list))
print(min(temp_list))

