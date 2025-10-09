def askDimension(PPrompt: str) -> float:
  Feed = input("Insert number: ")
  return Feed

Width = askDimension("width")
Height = askDimension("height")

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
  Area = float(PWidth) * float(PHeight)
  return Area

Area = calcRectangleArea(Width, Height)
print("")
print(f"Area is {Area}²")
print("end")