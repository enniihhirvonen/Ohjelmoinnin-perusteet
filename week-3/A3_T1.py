print("Program starting.")

print("Insert two integers.")
Feed=input("Insert first integer: ")
First=int(Feed)
Feed=input("Insert second integer: ")
Second=int(Feed)

print("Comparing inserted integers.")

if First > Second:
    print("First integer is greater.")

elif First < Second:
    print("Second integer is greater.")

elif First == Second:
    print("Integers are the same.")

Sum=(First + Second)

print("Adding integers together.")
print(f"{First} + {Second} = {Sum}")

print("Checking the parity of the sum...")

if Sum % 2 == 0:
    print("Sum is even.")

else:
    print("Sum is odd.")

print("Program ending.")