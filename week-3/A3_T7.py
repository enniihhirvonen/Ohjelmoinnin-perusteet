print("Program starting.\nTesting decision structures.")

Value=int(input("Insert an integer: "))

print("\nOptions:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")

Choice=int(input("\nYour choice: "))

if Choice == 1:
    if Value >= 400:
        Value += 44
    elif Value >= 200:
        Value += 22
    elif Value >= 100:
        Value += 11
    else:
        print("Integer stays the same.")

    print(f"Result is {Value}")

elif Choice == 2:
    if Value >= 400:
        Value += 44
    if Value >= 200:
        Value += 22
    if Value >= 100:
        Value += 11
    else:
        print("Value stays the same.")
    print(f"Result is {Value}")

elif Choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print("\nProgram ending.")