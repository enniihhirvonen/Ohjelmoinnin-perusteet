"""
NEEDED FUNCTIONS
main: include filename input
read_file: skip header row, if line is empty skip line
analyse_timestamps: count each row that starts with weekday
display_results

"""

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def read_file(filename: str, rows: list[str]):
    print(f"Reading file \"{filename}\".")

    rows.clear()

    with open(f"week-7/csv/{filename}", "r") as file:
        next(file)
        for line in file:
            if line.strip():
                rows.append(line.strip())

    return None

def analyse_timestaps(rows: list[str], results: list[str]):
    print("Analysing timestamps.")

    timestamp_amount = [0, 0, 0, 0, 0, 0, 0]

    for row in rows:
        if row.startswith(WEEKDAYS[0]):
            timestamp_amount[0] += 1
        elif row.startswith(WEEKDAYS[1]):
            timestamp_amount[1] += 1
        elif row.startswith(WEEKDAYS[2]):
            timestamp_amount[2] += 1
        elif row.startswith(WEEKDAYS[3]):
            timestamp_amount[3] += 1
        elif row.startswith(WEEKDAYS[4]):
            timestamp_amount[4] += 1
        elif row.startswith(WEEKDAYS[5]):
            timestamp_amount[5] += 1
        elif row.startswith(WEEKDAYS[6]):
            timestamp_amount[6] += 1

    results.extend(timestamp_amount)

    timestamp_amount.clear()

    return None

def display_results(results: list[str]):
    print("Displaying results.")

    print("### Timestamp analysis ###")

    print(f"- {WEEKDAYS[0]} {results[0]} stamps")
    print(f"- {WEEKDAYS[1]} {results[1]} stamps")
    print(f"- {WEEKDAYS[2]} {results[2]} stamps")
    print(f"- {WEEKDAYS[3]} {results[3]} stamps")
    print(f"- {WEEKDAYS[4]} {results[4]} stamps")
    print(f"- {WEEKDAYS[5]} {results[5]} stamps")
    print(f"- {WEEKDAYS[6]} {results[6]} stamps")

    print("### Timestamp analysis ###")

    return None

def main():
    print("Program starting.")

    rows = []
    results = []

    filename = str(input("Insert filename: "))

    read_file(filename, rows)

    analyse_timestaps(rows, results)

    display_results(results)

    print("Program ending.")

    return None

if __name__ == "__main__":
    main()