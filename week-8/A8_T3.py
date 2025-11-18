import math
import statistics

def show_options():
    print("\nOptions:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")

    return None

def ask_choice():
    return int(input("Your choice: "))

def ask_filename():
    return input("Insert filename: ")

def read_values(filename, values):
    with open(f"week-8/txt/{filename}", "r") as file:
        for line in file:
            if line.strip():
                values.append(float(line))
                
    return None

def calculate_amount(values):
    return len(values)

def calculate_sum(values):
    return round(math.fsum(values), 1)

def calculate_average(values):
    return round(statistics.mean(values), 1)

def main():
    print("Program starting.")

    values = []

    while True:
        show_options()
        choice = ask_choice()

        if choice == 0:
            break
        elif choice == 1:
            values = []
            filename = ask_filename()
            read_values(filename, values)
        elif choice == 2:
            print(calculate_amount(values))
        elif choice == 3:
            print(calculate_sum(values))
        elif choice == 4:
            print(calculate_average(values))
        else:
            print("Invalid choice.")

    print("\nProgram ending.")

    return None

if __name__ == "__main__":
    main()