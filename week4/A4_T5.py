print("Program starting.")
print("")
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))
print("")
if start >= stop:
  print("Starting point value must be less than the stopping point value.")
if (inspect < start) or (inspect > stop):
  print("Inspection value must be within the range of start and stop.")
else:
  string = ""
  string2 = ""
  for i in range(start, stop):
    if inspect == i:
      break
    elif i == inspect-1: string += str(f"{i}")
    else: string += str(f"{i} ")
  print("First loop - inspection with break:")
  print(string)
  
  for i in range(start, stop):
    if inspect == i and len(string2) == 0:
      continue
    elif inspect == i:
      string2 += " "
      continue
    elif i == inspect-1: string2 += str(f"{i}")
    else: string2 += str(f"{i} ")
  print("Second loop - inspection with continue:")
  print(f"{string2}")

print("")  
print("Program ending.")