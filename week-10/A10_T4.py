"""
########################################################
# Task A10_T4
# Developer Enni Hirvonen
# Date 2025-12-05
########################################################

"""

import sys
from A10_TLib import readValues, displayValues, merge, mergeSort

def main():
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

    if len(sys.argv) == 2:
        Filename = sys.argv[1]
    else:
        Filename = input("Insert filename: ")

    readValues(Filename, Values)

    displayValues(Filename, Values)

    asc = mergeSort(Values)
    print(f"Ascending '{Filename}' -->", end = " ")
    print(*asc, sep = ", ")

    desc = mergeSort(Values, PAsc=False)
    print(f"Descending '{Filename}' -->", end = " ")
    print(*desc, sep = ", ")

    print("Program ending.")

if __name__ == "__main__":
    main()