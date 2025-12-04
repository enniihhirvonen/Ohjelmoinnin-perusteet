# main.py
"""
########################################################
# Task A10_T3
# Developer Enni Hirvonen
# Date 2025-12-04
########################################################

"""

import sys
from A10_TLib import readValues, displayValues, bubbleSort

def main() -> None:
    # Initialize
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

    # TODO: Handle CLI argument or prompt for filename
    # If len(sys.argv) == 2, use sys.argv[1]
    # Otherwise, ask the user to input the filename
    if len(sys.argv) == 2:
        Filename = sys.argv[1]
    else:
        Filename = input("Insert filename: ")

    # TODO: Read values from file into Values list using readValues()
    readValues(Filename, Values)

    # TODO: Print raw values using displayValues()
    displayValues(Filename, Values)

    # TODO: Sort values in ascending order using bubbleSort()
    # TODO: Print sorted ascending values
    bubbleSort(Values)
    print(f"Ascending '{Filename}' -->", end = " ")
    print(*Values, sep = ", ")

    # TODO: Sort values in descending order using bubbleSort(PAsc=False)
    # TODO: Print sorted descending values
    bubbleSort(Values, PAsc=False)
    print(f"Descending '{Filename}' -->", end = " ")
    print(*Values, sep = ", ")

    # Clear list
    Values.clear()

if __name__ == "__main__":
    main()