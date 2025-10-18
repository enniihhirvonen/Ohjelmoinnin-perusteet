def main():
    print("Program starting.")
    print("This program can copy a file.")
    
    source = input("\nInsert source filename: ")
    destination = input("Insert destination filename: ")

    copyFile(source, destination)

    print("\nProgram ending.")

def copyFile(source, destination):
    print(f"\nReading file \'{source}\' content.")

    readFile = open(f"D:/School/2025/Ohjelmointi/Ohjelmoinnin-perusteet/week-6/txt/{source}", "r")

    print("\nFile content ready in memory.")

    print(f"\nWriting content into file \'{destination}\'")

    writeFile = open(f"D:/School/2025/Ohjelmointi/Ohjelmoinnin-perusteet/week-6/txt/{destination}", "w")

    while True:
        line = readFile.readline()
        writeFile.write(line)
        if len(line) == 0:
            break

    readFile.close()
    writeFile.close()

    print("\nCopying operation complete.")

    return None

main()