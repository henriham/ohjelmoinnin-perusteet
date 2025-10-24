
def analyzer():
  acc = []
  name = ""

  filename = input("Insert filename to read: ")
  file = open(filename, "r")
  lines = file.readlines()
  print("Analysing names...")
  for i, line in enumerate(lines):
    if len(line.strip()) == 0:
      continue
    name += str(f'{line.strip()};')
    acc.append(line.strip())
  file.close()

  print("### REPORT BEGIN ###")
  print(f"Name count -  {i}")
  print(f"Shortest name - {min(len(w) for w in acc)} chars")
  print(f"Longest name - {max(len(w) for w in acc)} chars")
  print(f"Average name - {sum(len(w) for w in acc)/(len(acc)):.2f}")
  print("### REPORT END ###")
  
def main():
  print("Program starting.\nThis program analyzes a list of names from a file.")
  analyzer()
  print("Program ending.")

main()