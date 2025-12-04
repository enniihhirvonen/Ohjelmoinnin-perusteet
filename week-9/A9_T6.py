"""
########################################################
# Task A9_T6
# Developer Enni Hirvonen
# Date 2025-12-02
########################################################

"""

def showOptions() -> None:
    print("Options:")
    print("1- Insert line")
    print("2- Save lines")
    print("0- Exit")

    return None

def askChoice() -> int:
    # TODO: Ask user for a menu choice and return it as an integer
    # Students should use try-except to handle invalid input

    try:
        feed = int(input("Your choice: "))
        return feed
    except ValueError:
        pass

    return -1

def saveLines(PLines: list[str]) -> None:
    # TODO: Ask for filename and save lines to the file
    # Students should use try-except to handle file errors
    filename = input("Insert filename: ")

    try:
        with open(filename, "w", encoding='UTF-8') as file:
            file.writelines(PLines)
                
    except Exception:
        print("Unknown")

    return None

def insertLine(PLines: list[str]) -> None:
    # TODO: Ask user to input a line and add it to PLines
    line = input("Insert text: ")
    PLines.append(line)

    return None

def onInterrupt(PLines: list[str]) -> None:
    # TODO: Handle KeyboardInterrupt when there are unsaved lines
    # Students should use try-except to handle input errors
    while True:
        try:
            save = input("Save before quit(y/n)?: ")
            if save == "y":
                saveLines(PLines)
                break
            elif save == "n":
                break
            else:
                raise ValueError
        except ValueError:
            print("Unknown option!")

    return None

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    # Wrap the main loop in a try-except block to catch KeyboardInterrupt
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        if not Lines == []:
            print("^CKeyboard interrupt and unsaved progress!")
            onInterrupt(Lines)
        else:
            print("^CClosing suddenly.")

    Lines.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()