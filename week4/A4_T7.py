print("Program starting.")
print("")
print("Check multiplicative persistence.")
number = int(input("Insert an integer: "))
digits = []
string = ""
acc = 1

for i in str(number):
  digits.append(int(i))
for i in range(len(digits)):
  if i == len(digits) - 1:
    acc *= digits[i]
    string += f"{digits[i]} = {acc}"
  elif len(digits) > 0:
    string += f"{digits[i]} * "
    acc *= digits[i]
print(string)