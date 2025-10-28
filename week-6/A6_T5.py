def main():
    print("Program starting.")

    filename = input("Insert filename: ")

    values = readValues(filename)

    result = analyseValues(values)

    report(result)

    print("Program ending.")

def readValues(filename):
    file = open(f"{filename}", "r")

    values = [] 

    while True:
        line = file.readline()
        if len(line) == 0:
            break
        values.append(int(line))

    return values

def analyseValues(values):
    count = len(values)
    total = sum(values)
    greatest = max(values)
    average = (total / count)

    return f"Count;Sum;Greatest;Average\n{count};{total};{greatest};{average:.2f}\n" #returns results as formatted string

def report(result):
    print("#### Number analysis - START ####")
    print(result) # prints the formatted string
    print("#### Number analysis - END ####")

    return None

if __name__ == "__main__":
    main()