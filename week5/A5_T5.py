print("Program starting.")
current_word = ""
def options():
  global current_word
  if len(current_word) == 0:
    print("")
  print("Options:")
  print("1 - Insert word")
  print("2 - Show current word")
  print("3 - Show current word in reverse")
  print("0 - Exit")
  user_input = input("Your choice: ")
  int_input = int(user_input)
  if int_input == 0:
    print("Exiting Program.")
    print("")
    print("Program ending")
  elif int_input == 1:
    current_word = input("Insert word: ")
    options()
  elif int_input == 2:
    print(f'Current word - "{current_word}"')
    options()
  elif int_input == 3:
    print(f'Current word - "{current_word[::-1]}"')
    options()
  else:
    print("Unknown option! try again")
    options()
options()

  
  
  





