# A10_E1.py
import sys
from A10_ELib import readValues, displayValues, quickSort
from A10_ELib import plotNumbers # consider for testing

def main() -> None:
    # 1. Initialize
    Values: list[int] = []
    Filename = ""
    # 2. Operate
    print("Program starting.")
    if (len(sys.argv) == 2):
        Filename = sys.argv[1]
        print("The filename '{}' was passed via CLI.".format(Filename))
    else:
        Filename = input('Insert filename: ')
    readValues(Filename, Values)
    # plotNumbers(Values, Filename.split('.')[0] + "_raw")
    # plotNumbers(Values, Filename.split('.')[0] + "_sorted")
    print("Raw '{}' -> ".format(Filename), end='')
    displayValues(Values, Horisontally=True)
    quickSort(Values)
    print("Ascending '{}' -> ".format(Filename), end='')
    displayValues(Values, True)
    quickSort(Values, PAsc=False) # Sort in DESCending order
    print("Descending '{}' -> ".format(Filename), end='')
    displayValues(Values, True)
    # plotNumbers(Values, Filename.split('.')[0], True)
    # 3. Cleanup
    print("Program ending.")
    Values.clear()
    return None

main()