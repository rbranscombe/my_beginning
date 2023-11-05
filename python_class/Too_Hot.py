ambient_temp=float(input("What is the temperature outside? "))


lower_ambient = 65.0
upper_ambient = 75.0

#print(type(lower_ambient))
#print(type(upper_ambient))
#print(type(ambient_temp))


if  ambient_temp < lower_ambient:
	print("Cold as ice")
if ambient_temp >= lower_ambient:
	if ambient_temp <= upper_ambient:
		print("Just right")
	elif ambient_temp > upper_ambient:
		print("Too hot. Gotta run for shelter.")

