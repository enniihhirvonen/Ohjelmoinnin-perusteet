def main():
    print("\nOptions:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")

    global word

    choice=int(input("\nYour choice: "))

    if choice == 1:
        insertword()

    elif choice == 2:
        currentword()

    elif choice == 3:
        reverse()

    elif choice == 0:
        print()

    else:
        print("Invalid input.")

def insertword():
    global word
    word=input("\nInsert word: ")
    return main()

def currentword():
    global word
    print(f"\nCurrent word - \"{word}\"")
    return main()

def reverse():
    global word
    print(f"\nWord reversed - \"{word[::-1]}\"")
    return main()

word=""

print("Program starting.")

main()

print("Program ending.")