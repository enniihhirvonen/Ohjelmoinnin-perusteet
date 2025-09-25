print("Program starting.")
print("Welcome to the unit converted program!\nFollow the menu instructions below.")

print("\nOptions:")
print("1 - Length\n2 - Weight\n0 - Exit")

Choice=int(input("Your choice: "))

if Choice == 1:
    print("1 - Meters to kilometers\n2 - Kilometers to meters\n0 - Exit")
    ChoiceLength=int(input("Your choice: "))
    if ChoiceLength == 1:
        Meters=float(input("Insert meters: "))
        Kilometers=round(Meters / 1000, 1)
        print(f"{Meters} m is {Kilometers} km")

    elif ChoiceLength == 2:
        Kilometers=float(input("Insert kilometers: "))
        Meters=round(Kilometers * 1000, 1)
        print(f"{Kilometers} km is {Meters} m")

    elif ChoiceLength == 0:
        print("Exiting...")

    else:
        print("Unknown option.")

elif Choice == 2:
    print("1 - Grams to pounds\n2 - Pounds to grams\n0 - Exit")
    ChoiceWeight=int(input("Your choice: "))
    if ChoiceWeight == 1:
        Grams=float(input("Insert grams: "))
        Pounds=round(Grams / 453.6, 1)
        print(f"{Grams} g is {Pounds} lb")

    elif ChoiceWeight== 2:
        Pounds=float(input("Insert pounds: "))
        Grams=round(Pounds * 453.6, 1)
        print(f"{Pounds} lb is {Grams} g")

    elif ChoiceWeight == 0:
        print("Exiting...")

    else:
        print("Unknown option.")

elif Choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print("Program ending.")
