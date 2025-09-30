print("Program starting.")
print("")
str = ""
i = 0
while True:
  user_input = input("Insert word (empty stops): ")
  if len(user_input) == 0: break
  else:
    i += 1
    str += user_input
print("")
print("You inserted:")
print(f"- {i} words")
print(f"- {len(str)} characters")
print("")
print("Program ending.")