from drawLib import drawCircle, drawSquare, saveSvg, Drawing

def showOptions():
    print("\nOptions:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

    return None

def askChoice():
    return int(input("Your choice: "))

def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")

def askValue2(PPrompt: str) -> str:
    return input(f"{PPrompt}: ")

def main() -> None:
    print("Program starting.")

    Dwg = Drawing()

    while True:
        showOptions()
        choice = askChoice()

        match choice:
            case 1:
                print('Insert square')
                print('Insert square')
                left = int(askValue1("- Left edge position: "))
                top = int(askValue1("- Top edge position: "))
                sideLength = int(askValue1("- Side length: "))
                color = askValue1("- Fill color: ")
                strokeColor = askValue1("- Stroke color: ")
                drawSquare(Dwg, left, top, sideLength, color, strokeColor)
                
            case 2:
                print('Insert circle')
                centerX = int(askValue1("- Center X coord: "))
                centerY = int(askValue1("- Center Y coord: "))
                radius = int(askValue1("- Radius: "))
                color = askValue1("- Fill color: ")
                stroke = askValue1("- Stroke color: ")
                drawCircle(Dwg, centerX, centerY, radius, color, stroke)
                
            case 3:
                filename = askValue2("Insert filename: ")
                print(f'Saving file to "{filename}"')

                proceed = askValue2("Proceed (y/n)?: ")
                if proceed.lower() == "y":
                    saveSvg(Dwg, filename)
                    print("Vector saved successfully!")
                else:
                    print("Save cancelled.")

            case 0:
                print("Exiting program.")
                break
        print()

    print("Program ending.")

    return None