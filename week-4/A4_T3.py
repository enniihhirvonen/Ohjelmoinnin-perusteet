print("Program starting.\n")

StartingValue=int(input("Insert starting value: "))
StoppingValue=int(input("Insert stopping value: "))

print("\nStarting while-loop.")

#while starting value is less than stopping value, print starting value, increasing in 1 integer each time it prints
while StartingValue <= StoppingValue:
    print(StartingValue, end=" ")
    StartingValue += 1

print("\n\nProgram ending.")