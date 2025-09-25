print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

Choice=int(input("\nYour choice: "))

if Choice == 1:
    Celsius=float(input("Insert the amount of Celsius: "))
    Fahrenheit=round((Celsius * 1.8) + 32, 1)
    print(f"{Celsius} °C equals to {Fahrenheit} °F")

elif Choice == 2:
    Fahrenheit=float(input("Insert the amount of Fahrenheit: "))
    Celsius=round((Fahrenheit - 32) / 1.8, 1)
    print(f"{Fahrenheit} °F equals to {Celsius} °C")

elif Choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print("\nProgram ending.")