#Written by KopyrightKid
def temp_program():
	f_or_c = input("\nWhat unit is your temperature in? Farenheit (f) or Celsius (c): ")
	if f_or_c == "f":
		#convert into farenheit
		temp_value = input("\nEnter the value you that you wish to convert: ")
		temp_value = int(temp_value) - 32 
		temp_value = int(temp_value) * 5
		temp_value = int(temp_value) / 9
		print("\nYour Temperature in Celsius is: {}".format(int(temp_value)))
	elif f_or_c == "c":
		#convert to celsius 
		temp_value = input("\nEnter the value you that you wish to convert: ")
		temp_value = int(temp_value) * 1.8 + 32
		print("\nYour Temperature in Farenheit is {}".format(int(temp_value)))
temp_program()
#this is to prevent window from closing immediately
input("\nPress enter to exit")