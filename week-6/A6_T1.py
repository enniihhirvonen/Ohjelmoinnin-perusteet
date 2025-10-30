def main():
    print("Program starting.")
    print("This program can read a file.\n")

    feed = input("Insert filename: ")

    fileName = (f"week-6/txt/{feed}")

    readFile(fileName, feed) # made feed and fileName separate from each other so that START and END lines wouldnt be messy

    print("\nProgram ending.")

def readFile(fileName, feed):
    print(f"\n#### START \"{feed}\" ####")

    file = open(fileName, "r")

    while True:
        line = file.readline()
        if len(line) == 0:
            break
        print(line, end="")
    file.close()

    print(f"#### END \"{feed}\" ####")
    return None

main()
