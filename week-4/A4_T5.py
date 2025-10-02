print("Program starting.\n")

StartingPoint=int(input("Insert starting point: "))
StoppingPoint=int(input("Insert stopping point: "))
InspectionPoint=int(input("Insert inspection point: "))

Violation = False

print()

if (StartingPoint >= StoppingPoint):
    print("Starting point value must be less than the stopping point value.")
    Violation = True

if (InspectionPoint < StartingPoint) or (InspectionPoint > StoppingPoint):
    print("Inspection value must be within the range of start and stop.")
    Violation = True

if Violation == True:
    print()

else:
    print("First loop - inspection with break:")
    for Loop1 in range(StartingPoint, StoppingPoint + 1):
        if Loop1 == InspectionPoint:
            break
        print(Loop1, end=" ")

    print("\nSecond loop - inspection with continue:")
    for Loop2 in range(StartingPoint, StoppingPoint + 1):
        if Loop2 == InspectionPoint:
            continue
        print(Loop2, end=" ")

    print("\n")

print("Program ending.")
