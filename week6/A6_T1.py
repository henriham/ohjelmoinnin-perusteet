print("Program starting. \nThis program can read a file.")
filename = input('Insert filename: ')
file = open(filename, "r")
print(f'#### START "{filename}" ####')
while True:
  line = file.readline()
  if len(line) == 0:
    break
  else:
    print(line, end="")
print(f"\n#### END \"{filename}\"\nProgram ending.")