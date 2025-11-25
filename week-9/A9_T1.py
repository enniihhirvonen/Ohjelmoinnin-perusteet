def gather_values(values):
    while True:
        try:
            raw = input("Insert a floating-point value (0 to stop): ")
            value = float(raw)
            if value == 0:
                break
            values.append(value)
        except ValueError:
            print(f"\nError! '{raw}' couldn't be converted to float.")

def result(values):
    return print(f"\nFinal sum is {sum(values):.2f}")

def main():
    print("""
########################################################
# Task A9_T1
# Developer Enni Hirvonen
# Date 2025-11-25
########################################################""")
    
    values = []

    print("\nProgram starting.\n")

    gather_values(values)

    result(values)

    print("\nProgram ending.")

if __name__ == "__main__":
    main()