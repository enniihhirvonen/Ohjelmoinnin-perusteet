"""
NEEDED FUNCTIONS
main for logic
input
output
"""

def prompt_input():
    values = []

    while True:
        value = int(input("Insert positive integer(negative stops): "))
        if value < 0:
            break
        values.append(value)

    return values

def results(values):
    if len(values) == 0:
        print("No integers to display.")
        return

    print(f"Displaying {len(values)} integers:")

    i = 0

    for value in values:
        o = (i + 1)
        
        print(f"- Index {i} => Ordinal {o} => Integer {values[i]}")

        i += 1

    return None
    
def main():
    print("Program starting.")
    print("Collect positive integers.")

    values = prompt_input()

    print("Stopped collecting positive integers.")

    results(values)

    print("Program ending.")

if __name__ == "__main__":
    main()