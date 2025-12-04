"""
########################################################
# Task A10_T2
# Developer Enni Hirvonen
# Date 2025-12-04
########################################################

"""

import sys # for possible exit on errors
import math

def readValues(PFilename: str, PValues: list[int]) -> None:
    # ...
    try:
        with open(f"week-10/{PFilename}", "r") as file:
            for line in file:
                if line.strip():
                    PValues.append(int(line.strip()))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

    return None

def sumOfValues(PValues: list[int]) -> int:
    # ...
    return sum(PValues)

def productOfValues(PValues: list[int]) -> int:
    # ...
    return math.prod(PValues)

def main() -> None:
    # 1. Initialize
    Values: list[int] = []
    # 2. Operate
    print("Program starting.")

    try:
        # 2.1 ask filename
        filename = input("Insert filename: ")
        # 2.2 read values
        readValues(filename, Values)
        # 2.3 calculate sum of values
        Sum = sumOfValues(Values)
        # 2.4 calculate product of values
        Product = productOfValues(Values)
        # 2.5 display results
        print("# --- Sum of numbers --- #")
        print(Sum)
        print("# --- Sum of numbers --- #")
        print("# --- Product of numbers --- #")
        print(Product)
        print("# --- Product of numbers --- #")

    except Exception as e:
        print(f"Error: {e}")
        pass

    # 3. Cleanup
    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()