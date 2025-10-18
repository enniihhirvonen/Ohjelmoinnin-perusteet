def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    fileName = input("\nInsert filename to read: ")

    analysis(fileName)

    results = analysis(fileName)

    report(results)

    print("\nProgram ending.")

def analysis(fileName):
    print("\nAnalysing names...")

    file = open(f"D:/School/2025/Ohjelmointi/Ohjelmoinnin-perusteet/week-6/txt/{fileName}", "r")
    
    while True:
        lines = file.readline()
        break

    names = []

    for line in lines:
        names.extend(line.strip().split())

    nameCount = len(names)
    charCount = sum(len(names) for names in line)
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
    }

def report(results):

    print("#### REPORT BEGIN ####")

    print(f"Name count - {results["nameCount"]}")
    print(f"Shortest name - {results["shortestName"]}")
    print(f"Longest name - {results["longestName"]}")
    print(f"Average name - {results["averageName"]}")

    print("#### REPORT END ####")

main()