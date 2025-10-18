def main():
    print("Program starting.\n")
    
    firstName = input("Insert first name: ")
    lastName = input("Insert last name: ")
    fileName = input("Insert filename: ")

    writeFile(firstName, lastName, fileName)

    print("\nProgram ending.")


def writeFile(firstName, lastName, fileName):
    file = open(f"D:/School/2025/Ohjelmointi/Ohjelmoinnin-perusteet/week-6/txt/{fileName}", "w")
    file.write(firstName + "\n")
    file.write(lastName + "\n")
    file.close()
    return None

main()