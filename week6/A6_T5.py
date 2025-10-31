def filehandler():
  filename = input("Insert filename: ")
  file = open(filename, 'r')
  data = [int(x.strip()) for x in file.readlines()]
  file.close()
  return data, filename
  
def analyser():
  data, filename = filehandler()
  count = len(data)
  summ = sum(data)
  greatest = max(data)
  average = summ / count
  print("#### Number analysis - START ####")
  print(f"File \"{filename}\" results:")
  print("Count;Sum;Greatest;Average")
  print(f"{count};{summ};{greatest};{average:.2f}")
  print("\n#### Number analysis - END ####")

def main():
  print("Program starting.")
  analyser()
  print("Program ending.")

main()