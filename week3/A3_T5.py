print("Program starting.")
print("")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
user_choice = float(input("Your choice: "))
if user_choice == 0:
	print("")
	print("Exiting...")
elif user_choice == 1:
	user_input = float(input("Insert the amount of Celsius: "))
	print(f"{user_input:.1f} °C equals to {1.8*user_input+32:.1f} °F")
elif user_choice == 2:
	user_input = float(input("Insert the amount of Fahrenheit: "))
	print(f"{user_input:.1f} °F equals to {((user_input-32)/1.8):.1f} °C")
print("")
print("Program ending.")