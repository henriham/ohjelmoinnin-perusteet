print("Program starting.")
number = int(input("Insert a positive integer: "))
string = ""
i = 0
while number >= 1:
  if number % 2 == 1 and number != 1:
    i += 1
    string += str(f"{number:.0f} -> ")
    number = (3 * number + 1)
  elif number % 2 == 0:
    i += 1
    string += str(f"{number:.0f} -> ")
    number = number / 2
  elif number == 1:
    string += str(f"{number:.0f}")
    print(string)
    print(f"Sequence had {i} total steps.")
    break
print("")
print("Program ending.")