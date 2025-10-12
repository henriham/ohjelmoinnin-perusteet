print("Program starting.")
count = 0
startedOnce = False
def showOptions():
  global startedOnce
  if startedOnce == True: print("")
  print("Options:")
  print("1 - Show count")
  print("2 - Increase count")
  print("3 - Reset count")
  print("0 - Exit")
  startedOnce = True
  return None

def askChoice():
  return input("Your choice: ")

def main():
  global count
  showOptions()
  feed = askChoice()
  if feed.isnumeric():
    if feed == '0':
      print("Exiting program.")
    elif feed == '1':
      print(f'Current count - {count}')
      main()
    elif feed == '2':
      print(f'Count increased!')
      count += 1
      main()
    elif feed == '3':
      print('Cleared count!')
      count = 0
      main()
    else:
      print("Unknown option!")
      main()
  else:
    print("Unknown option!")
    main()
  
main()
print("")
print("Program ending.")
