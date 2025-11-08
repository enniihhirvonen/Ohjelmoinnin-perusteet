"""
NEEDED FUNCTIONS
input + input validation, error message for invalid
sum calculcation
results
if no valid integers, show message and end

"""

def prompt_input():
    values = []

    value = str(input("Insert comma separated integers: "))

    values.extend(value.strip().split(",")) # adds input to list, seperating by comma

    return values

def validate_input(values):
    valid_values = []
    invalid_values = []

    for value in values:
        if value.isnumeric():
            valid_values.append(value)
        else:
            invalid_values.append(value)

    if valid_values == []:
        print("No values to analyse.")
        return None
    
    if invalid_values:
        print(f"Invalid value(s) \"{", ".join(invalid_values)}\" detected.") # .join ensures the invalid values are printed out correctly here

    print(f"There are {len(valid_values)} integers in the list.")

    return valid_values

def calculate_sum(valid_values):
    int_values = [int(value) for value in valid_values] # changes strings in list to integers to allow for summing them up

    return sum(int_values)

def results(summed_value):
    if (summed_value % 2 == 0):
        odd_or_even = "even"
    else:
        odd_or_even = "odd"

    print(f"Sum of the integers is {summed_value} and it's {odd_or_even}.")


def main():
    print("Program starting.")

    values = prompt_input()

    new_values = validate_input(values)

    if new_values == None: # if there are no valid values returned, end the program immediately
        print("Program ending.")
        return

    summed_value = calculate_sum(new_values)

    results(summed_value)
    
    print("Program ending.")

if __name__ == "__main__":
    main()