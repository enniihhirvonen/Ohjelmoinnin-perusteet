print("Program starting.\nThis is a program with simple menu, where you can choose which operation the program performs.")
Name=input("Before the menu, please insert your name: ")
print()
print("Options:\n 1: Print welcome message\n 0: Exit\n")
Choice=int(input("Your choice: "))

if Choice == 1:
    print(f"Welcome, {Name}!")

elif Choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print("Program ending.")