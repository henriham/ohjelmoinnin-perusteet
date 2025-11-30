
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
    elif len(nums) == 0:
      print("No integers to display.")
      print("Stopped collecting positive integers.")
      break
    else:
      print("Stopped collecting positive integers.")
      break
    if len(nums) > 0:
      print(f"Displaying {(len(nums))} integers:")
  for i in range(len(nums)):
    print(f" Index {i} => Ordinal {i+1} => Integer {nums[i]}")

  print("Program ending.")

if __name__ == "__main__":
  main()