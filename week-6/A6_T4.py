def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    fileName = input("\nInsert filename to read: ")

    results = analysis(fileName)

    report(results)

    print("\nProgram ending.")

def analysis(fileName):
    print("\nAnalysing names...")

    file = open(f"week-6/txt/{fileName}", "r")

    names = []
    
    while True:
        line = file.readline()
        if not line: # if the line is empty, break the loop
            break

        line = line.strip() # strip line of whitespace

        if line: # if line is not empty after stripping, split names based on whitespace
            names.append(line) # add names to list

    file.close()

    nameCount = len(names)
    charCount = sum(len(name) for name in names)
    shortestName = min(names, key=len)
    longestName = max(names, key=len)
    averageName = (charCount / nameCount)

    print("\nAnalysis complete!")

    return {
        "nameCount": nameCount,
        "charCount": charCount,
        "shortestName": shortestName,
        "longestName": longestName,
        "averageName": averageName,
    } # returns results as dictionary

def report(results):

    print("#### REPORT BEGIN ####")

    print(f"Name count - {results["nameCount"]}")
    print(f"Shortest name - {results["shortestName"]}")
    print(f"Longest name - {results["longestName"]}")
    print(f"Average name - {results["averageName"]}")

    print("#### REPORT END ####")

main()