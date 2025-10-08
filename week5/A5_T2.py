def frameWord(input):
    asterisks = ""
    for index, i in enumerate(input):
      asterisks += f"*"
    print(f"**{asterisks}**")
    print(f"* {input} *")
    print(f"**{asterisks}**")

def main():
  print("Program starting.")
  Pword =  input("Insert word: ")
  print("")
  frameWord(Pword)
  print("")
  print("Program ending.")
  
  return None

  
main()