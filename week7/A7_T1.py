
def collectPosInt():
  feed = int(input("Insert positive integer(negative stops): "))
  return feed

def main():
  print("Program starting.")
  print("Collcet positive integers.")
  nums: list[int] = []

  while True:
    feed = collectPosInt()
    if feed > -1:
      nums.append(feed)
    else:
      break
  print(f"Displaying {(len(nums))} integers:")
  for i in range(len(nums)):
    print(f" Index {i} => Ordinal {i+1} => Integer {nums[i]}")

  print("Program ending.")

if "__NAME__":
  main()
