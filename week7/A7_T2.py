
def collectNumbers():
  feed = input("Insert comma separated integers: ")
  feed = feed + ","
  arr = []
  acc = ""
  if len(feed) == 0:
    return []
  else:
    for n in feed:
      if n == ",":
        arr.append(acc)
        acc = ""
      else:
        acc += n
  return arr

def processList():
  nums = collectNumbers()
  finaList = []
  for n in nums:
    if n == "" and len(nums) == 1:
      print("No values to analyse.")
      return
    elif len(nums) == 1 and not n.isnumeric():
      print(f"Invalid value '{n}' detected.")
      print("No values to analyse.")
    elif n.isnumeric():
      finaList.append(int(n))
    else:
      print(f"Invalid value '{n}' detected.")
  return finaList

def main():
  print("Program starting.")
  nums: list[int] = []
  nums = processList()
  if nums:
    isEven = "even"
    if sum(nums) % 2 != 0:
      isEven = "odd"
    print(f"There are {len(nums)} integers in the list.")
    print(f"Sum of the integers is {sum(nums)} and it's {isEven}")
  
  print("Program ending.")
  

if __name__ == "__main__":
  main()