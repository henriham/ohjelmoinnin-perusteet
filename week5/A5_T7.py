print("Program starting.")
DELIMITER = ","
acc = ""
i = 0
def collectWords():
  global acc
  global i
  word = input("Insert word(empty stops): ")
  if len(word) == 0:
    acc += ""
    analyzeWords()
  else:
    i += len(word)
    acc += word+DELIMITER
    collectWords()

def analyzeWords():
  count = acc.count(',')
  Avg = i / count
  print(f"- {count} Words")
  print(f"- {i} Characters")
  print("-{:.2f} - Average word length".format(Avg))
  
def main():
  collectWords()

main()
print("Program ending.")