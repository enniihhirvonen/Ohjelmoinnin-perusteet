print("Program starting.\n")

print("Check multiplicative persistence.")

Value=int(input("Insert an integer: "))

Steps=[] #list for tracking steps

Product= 1

while (Value > 10):
    Digits=[int(d) for d in str(Value)] #creates list for each digit in Value (which has been converted to string to allow this) -> then converts each digit back to integers in order for multiplication to take place
    for d in Digits:
        Product *= d

AAAAAAAAAAAAAAA


print("No more steps.")

print(f"\nThis program took () steps.")

print("\nProgram ending.")