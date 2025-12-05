def merge(PLeft: list[int], PRight: list[int], PAsc: bool = True) -> None:
    result = []
    while PLeft and PRight:
        if PAsc:
            if PLeft[0] < PRight[0]:
                result.append(PLeft.pop(0))
            else:
                result.append(PRight.pop(0))
        else:
            if PLeft[0] > PRight[0]:
                result.append(PLeft.pop(0))
            else:
                result.append(PRight.pop(0))

    result.extend(PLeft)
    result.extend(PRight)

    return result

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    # Sort PValues.
    # PAsc: in ascending order by default. False will sort in descending order.

    if len(PValues) <= 1:
        return PValues
    
    mid = int(len(PValues) / 2)
    left = mergeSort(PValues[0:mid], PAsc)
    right = mergeSort(PValues[mid:], PAsc)

    return merge(left, right, PAsc)

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    # Sort PValues by implementing bubble sort algorithm.
    # Handle PValues list like it is a pointer to memory
    # Sort the list inplace e.g., PValues[CurrentIndex] = PValues[NextIndex]
    # Don't overwrite PValues identifier.
    # Tester expects that the PValues list is modified.
    # It doesn't catch a return value.

    n = len(PValues)

    # outer loop for passes
    for i in range(n):
        # inner loop for comparisons
        for j in range(0, n - i - 1):
            if PAsc:
                if PValues[j] > PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j +1], PValues[j]
            else:
                if PValues[j] < PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j +1], PValues[j]

    return None

def readValues(PFilename, PValues):
    try:
        with open(PFilename, "r") as file:
            for line in file:
                if line.strip():
                    PValues.append(int(line.strip()))
    except Exception as e:
        raise

def displayValues(PFilename, PValues):
    print(f"Raw '{PFilename}' -->", end = " ")
    print(*PValues, sep = ", ")