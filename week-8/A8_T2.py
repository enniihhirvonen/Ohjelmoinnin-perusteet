import A8_T2_library

def show_options():
    print("\nOptions:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def ask_choice():
    return int(input("Your choice: "))

def ask_value(choice):
    options = [
        ["addend", "addend"],
        ["minuend", "subtrahend"],
        ["multiplicant", "multiplier"],
        ["dividend", "divisor"]
        ]
    
    value1 = float(input(f"Insert first {options[choice - 1][0]} value: "))
    value2 = float(input(f"Insert second {options[choice - 1][1]} value: "))

    return value1, value2

def main():
    print("Program starting.")

    while True:
        show_options()

        choice = ask_choice()
        if choice == 0:
            break

        value1, value2 = ask_value(choice)

        if choice == 1:
            result = A8_T2_library.add(value1, value2)
            print(f"{value1} + {value2} = {result}")
        elif choice == 2:
            result = A8_T2_library.subtract(value1, value2)
            print(f"{value1} - {value2} = {result}")
        elif choice == 3:
            result = A8_T2_library.multiply(value1, value2)
            print(f"{value1} * {value2} = {result}")
        elif choice == 4:
            result = A8_T2_library.divide(value1, value2)
            print(f"{value1} / {value2} = {result}")

print("\nProgram ending.")

if __name__ == "__main__":
    main()
