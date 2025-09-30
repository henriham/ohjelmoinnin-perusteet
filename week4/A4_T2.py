print("Program starting.")
print("")
start_val = int(input("Insert starting value: "))
stop_val = int(input("Insert stopping value: "))
print("")
print("Starting for-loop:")
i_str = ""
for i in range(start_val, stop_val+1):
	if i < stop_val: i = str(f"{i} ")
	else: i = str(f"{i}")
	i_str += i	
print(i_str)
print("")
print("Program ending.")