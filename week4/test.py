count = int(input("loop count:"))
string = ""
i = 0
while True:
  if i == count: break
  elif i == count-1:
    i += 1
    string += str(f"{i}")
  else: 
    i += 1
    string += str(f"{i}.") 
print(string)