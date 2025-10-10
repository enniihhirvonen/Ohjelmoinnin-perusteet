# def askDimension(PPrompt: str) -> float:
#    Feed = input("Insert number: ")
#    return Feed

# Width = askNumber("width")
# Height = askNumber("height")

# def calcRectangleArea(PWidth: float, PHeight: float) -> float:
#    PWidth = Area * PHeight
#    return Sum

# Area = calculateArea()
# print("")
# print("Area is {Area}²")
# print("end")

def askDimension(PPrompt: str) -> float:
    Feed = float(input(f"Insert {PPrompt}: "))
    return Feed

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    Area = (PWidth * PHeight)
    return Area

def main():
    print("Program starting.")
    PWidth = askDimension("width")
    PHeight = askDimension("height")
    Area = calcRectangleArea(PWidth, PHeight)
    print()
    print(f"Area is {Area}²")
    print("Program ending.")

main()