LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def writeFile(filename, content):
  file = open(filename, 'w', encoding="UTF-8")
  file.write(content)
  file.close()
  print("Ciphered text saved!")
  return None

def askRows():
  inputStr = ""
  while True:
    feed = input("Insert row(empty stops): ")
    if len(feed) == 0:
      return inputStr
    else:
      inputStr += feed + "\n"

def shiftCharacter(char, alphabet, shift=13):
  if char in alphabet:
    index = alphabet.index(char)
    return alphabet[(index + shift) % len(alphabet)]
  else:
    return char

def rot13(inputStr):
  rot13str = ""
  for char in inputStr:
    if char.islower():
      rot13str += shiftCharacter(char, LOWER_ALPHABETS)
    elif char.isupper():
      rot13str += shiftCharacter(char, UPPER_ALPHABETS)
    else:
      rot13str += char
  return rot13str

def main():
  print("Program starting.\n")
  print("Collecting plain text rows for ciphering.")
  data = askRows()
  ciphered = rot13(data)
  print("\n#### Ciphered text ####")
  print(ciphered)
  print("#### Ciphered text ####")
  filename = input("Insert filename to save: ")
  if filename:
    writeFile(filename, ciphered)
  else:
    print("File name not defined.\nAborting save operation.")
  print("Program ending.")
  return None

if __name__ == "__main__":
  main()
