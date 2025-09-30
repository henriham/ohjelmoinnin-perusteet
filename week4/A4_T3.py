print("Program starting.")
print("")
start_val = int(input("Insert starting value:"))-1
stop_val = int(input("Insert stopping value:"))
string = ""
while True:
  if stop_val == start_val: break
  elif start_val == stop_val-1: 
    start_val += 1
    string += str(f"{start_val}")
  else:
    start_val += 1
    string += str(f"{start_val} ")
print("")
print("Starting while-loop:")
print(f"{string}")
print("")
print("Program ending.")