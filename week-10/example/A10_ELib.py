"""
Program modularity was introduced in the A8.

This program file acts as a program library containing different
functionalities for the other programs to consume.

In CG, for the actual returns, you can create "A10_TLib.py".
Then in the different returns utilize the same library file again and again.

e.g.

# A10_T3.py
from A10_TLib.py import readValues

    # ...
    Values: list[int] = []
    Filename = input("Insert filename: ")
    readValues(Filename, Values)
"""
import sys
import matplotlib.pyplot as plt

def readValues(PFilename: str, PValues: list[int]) -> None:
    PValues.clear()
    try:
        Filehandle = open(PFilename, 'r', encoding="UTF-8")
        while True:
            Line = Filehandle.readline() # Read line and move stream position to next line
            if (len(Line) == 0): # File ends
                break
            elif (Line == '\n'): # Empty line
                continue
            else:
                Row = Line.rstrip('\n') # This right strip removes newline from the right side 
                Value = int(Row) # Convert string to integer
                PValues.append(Value)
        Filehandle.close() # Vapautetaan varatut resurssit takaisin järjestelmälle
    except Exception:
        print("Couldn't read file '{}'.".format(PFilename))
        sys.exit(1) # 1 - virhetilanne
    return None

def partition(PArr: list[int], PLow: int, PHigh: int, PAsc: bool) -> int:
    # Choose the last element as pivot
    Pivot = PArr[PHigh]
    i = PLow - 1  # Pointer for the smaller element
    for j in range(PLow, PHigh):
        # If current element is smaller than or equal to the pivot
        if (PArr[j] <= Pivot and PAsc) or (PArr[j] >= Pivot and not PAsc):
            i += 1
            # Swap the elements
            TempElem = PArr[i]
            PArr[i] = PArr[j]
            PArr[j] = TempElem
    # Swap the pivot element with the element at i + 1
    TempElem = PArr[i + 1]
    PArr[i + 1] = PArr[PHigh]
    PArr[PHigh] = TempElem
    # Set pivot index
    PivotIndex = i + 1
    return PivotIndex

def quickSort(PArr: list[int], PLow: int = None, PHigh: int = None, PAsc: bool = True) -> None:
    if PLow == None: PLow = 0
    if PHigh == None: PHigh = len(PArr) - 1
    if PLow < PHigh:
        # Partition the array and get the pivot index
        PivotIndex = partition(PArr, PLow, PHigh, PAsc)
        # Recursively apply quick sort to the left and right subarrays
        quickSort(PArr, PLow, PivotIndex - 1, PAsc)
        quickSort(PArr, PivotIndex + 1, PHigh, PAsc)
    return None

def plotNumbers(PNumbers: list[int], PTitle: str, Save=True) -> None:
    xAxis = [(i + 1) for i in range(len(PNumbers))]
    plt.plot(xAxis, PNumbers)
    plt.ylabel("Value")
    plt.title(PTitle)
    if Save:
        plt.savefig(PTitle + '.png')
    else:
        plt.show()
    plt.clf() # Clear current figure
    return None

def displayValues(Values: list[str|int|float], Horisontally=False) -> None:
    for i, Value in enumerate(Values):
        if Horisontally:
            if i == len(Values) - 1:
                print(Value)
            else:
                Part = str(Value) + ", "
                print(Part, end='')
        else:
            print(Value)
    return None