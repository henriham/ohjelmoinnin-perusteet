print("Program starting.")
print("Testing decision structures")
value = int(input("Insert an integer: "))
print("Options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")
user_choice = int(input("Your choice: "))
if user_choice not in (0, 1, 2): print("Unknown option.")
elif user_choice == 0: print("Exiting...")
elif user_choice == 1:
  if value >= 400: value += 44
  elif value >= 200: value += 22
  elif value >= 100: value += 11
  print("Using one multi-branched decision structure.")
  print(f"Result is {value}")
elif user_choice == 2:
  if value >= 100: value += 11
  if value >= 200: value += 22
  if value >= 400: value += 44
  print("Using multiple independent if-statements structure.")
  print(f"Result is {value}")

print("")
print("Program ending.")