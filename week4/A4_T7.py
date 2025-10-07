print("Program starting.")
print("")
print("Check multiplicative persistence.")
number = int(input("Insert an integer: "))
step = 0
while number >= 10:
  string = ""
  acc = 1
  for index, i in enumerate(str(number)):
    if index == len(str(number))-1:
      acc *= int(i)
      string += f"{i} = {acc}"
      number = acc
      step += 1
    else:
      acc *= int(i)
      string += f"{i} * "
  print(string)
print("No more steps.")
print("")
print(f"This program took {step} step(s)")
print("")
print("Program ending.")

