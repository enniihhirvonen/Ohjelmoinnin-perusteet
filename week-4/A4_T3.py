print("Program starting.\n")

StartingValue=int(input("Insert starting value: "))
StoppingValue=int(input("Insert stopping value: "))

print("\nStarting while-loop.")

#as long as starting value is less than stopping value, print starting value increasing by 1 each time it prints
while StartingValue <= StoppingValue:
    print(StartingValue, end=" ")
    StartingValue += 1

print("\n\nProgram ending.")