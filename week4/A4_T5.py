print("Program starting.")
print("")
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))

if start >= stop:
  print("")
  print("Starting point value must be less than the stopping point value.")
elif (inspect < start) or (inspect > stop):
  print("")
  print("Inspection value must be within the range of start and stop.")
else:
  string = ""
  for i in range(start, stop):
    if inspect == i:
      break
    elif i == inspect-1: string += str(f"{i}")
    else: string += str(f"{i} ")
  print("First loop - inspection with break:")
  print(string)
print("")  
print("Program ending.")