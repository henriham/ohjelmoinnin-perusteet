LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def writeFile(Pdata):
  filename = input("Insert filename to save: ")
  if filename:
    file = open(filename, "w")
    file.write(Pdata)
    file.close()
    print("Ciphered text saved!")
  else:
    print("File name not defined.\nAborting save operation.")
  return None

def askRows():
  inputStr = ""
  while True:
    feed = input("Insert row(empty stops): ")
    if len(feed) == 0:
      return inputStr
    else:
      inputStr += feed + "\n"

def shiftCharacter(input):
  if input.islower():
    for index, char in enumerate(LOWER_ALPHABETS):
      if input == LOWER_ALPHABETS[index]:
        return LOWER_ALPHABETS[(index + 13) % len(LOWER_ALPHABETS)]
  elif input.isupper():
    for index, char in enumerate(UPPER_ALPHABETS):
      if input == UPPER_ALPHABETS[index]:
        return UPPER_ALPHABETS[(index + 13) % len(UPPER_ALPHABETS)]
  else:
    return input

def rot13(inputStr):
  #string = sana;jotai;muuta;
  rot13str = ""
  for char in inputStr:
    if char == ";":
      rot13str += "\n"
    else:  
      rot13str += shiftCharacter(char)
  return rot13str

def main():
  print("Program starting.\n")
  data = askRows()
  print("\n#### Ciphered text ####")
  print(rot13(data))
  print("#### Ciphered text ####")
  writeFile(rot13(data))
  print("Program ending.")

if __name__ == "__main__":
	main()