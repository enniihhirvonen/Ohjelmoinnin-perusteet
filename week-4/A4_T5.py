print("Program starting.\n")

StartingPoint=int(input("Insert starting point: "))
StoppingPoint=int(input("Insert stopping point: "))
InspectionPoint=int(input("Insert inspection point: "))

Violation = False #violation flag tracks if violation has been made in inputs

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
    for i in range(StartingPoint, StoppingPoint + 1):
        if i == InspectionPoint:
            break #when loop reaches inspection value, end loop
        print(i, end=" ")

    print("\nSecond loop - inspection with continue:")
    for i in range(StartingPoint, StoppingPoint + 1):
        print(i, end=" ")

    print("\n")

print("Program ending.")
