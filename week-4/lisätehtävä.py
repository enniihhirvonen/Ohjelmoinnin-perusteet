print("Program starting.\n")

Username=input("Insert username: ")

if (Username != "Rain"):
    print("\nWrong name, access blocked.")
    print("\nProgram ending.")
    quit()

Age=int(input("Insert your age: "))

if (Age < 18):
    print("\nInsufficient age, access blocked.")
    print("\nProgram ending.")
    quit()

Admin=input("Are you an admin? (y/n): ")

if (Username == "Rain") and (Age >= 18) and (Admin == "y"):
    print("Loading admin page...")
    print("\nOptions:")
    print("1 - Add new user")
    print("2 - Check performance of device")
    print("3 - Exit")

elif (Username == "Rain") and (Age >= 18) and (Admin != "y"):
    print("Loading user page...")
    print("\nOptions:")
    print("1 - Check your info")
    print("2 - Exit")





