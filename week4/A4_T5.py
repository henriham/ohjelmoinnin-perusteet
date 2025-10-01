print("Program starting.")
print("")
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))
string = ""
for i in range(start, stop):
  if inspect == i:
    break
  elif start >= stop:
    print("")
    print("Starting point value must be less than the stopping point value.")
    break
  elif inspect not in (i):
    print("Inspection value must be within the range of start and stop.")
    break
  
  elif i == inspect-1: string += str(f"{i }")
  else: string += str(f"{i }")

print(string)
print("Program ending.")