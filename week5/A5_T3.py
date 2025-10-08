def askName():
  Pname = input("Insert name: ")
  return Pname

def greetUser(Pname):
  print(f"Hello {Pname}!")
  return None

def main():
  print("Program starting")
  greetUser(askName())
  print("Program ending")
  return None

main()