def main():
    print("Program starting.")

    global count #changing count to a global variable

    while True: #loops options + choice input
        showoptions()
        choice=askchoice()

        if choice is not None:
            if choice == "1":
                showcount()

            elif choice == "2":
                increasecount()

            elif choice == "3":
                resetcount()

            elif choice == "0":
                print("Exiting program.\n")
                break

    print("Program ending.")

def showoptions():
    print("\nOptions:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askchoice():
    choice=input("\nYour choice: ")
    x=choice.isnumeric()
    if (x == False) or (choice not in ["1", "2", "3", "0"]): #checks with isnumeric() + in list for acceptable inputs
        print("Unknown option!")
        return None #returns None when input is invalid
    return choice #if valid, return choice
    
def showcount():
    global count
    print(f"Current count - {count}")

def increasecount():
    global count
    count += 1
    print("Count increased!")

def resetcount():
    global count
    count = 0
    print("Cleared count!")

count = 0 #initializes count

main()