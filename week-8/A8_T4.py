from datetime import datetime

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

def show_options():
    print("\nOptions:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

    return None

def ask_choice():
    return int(input("Your choice: "))

def read_file(filename, timestamps):
    with open(f"week-8/txt/{filename}", "r") as file:
        for line in file:
            if line.strip():
                ts = datetime.fromisoformat(line.strip())
                timestamps.append(ts)

    return None

def calculate_years(year, timestamps):
    return sum(1 for ts in timestamps if ts.year == year)

def calculate_months(month, timestamps):
    month_index = MONTHS.index(month) + 1
    return sum(1 for ts in timestamps if ts.month == month_index)

def calculate_weekdays(weekday, timestamps):
    weekday_index = WEEKDAYS.index(weekday)
    return sum(1 for ts in timestamps if ts.weekday() == weekday_index)

def main():
    print("Program starting.")

    timestamps = []

    filename = input("Insert filename: ")

    read_file(filename, timestamps)

    while True:
        show_options()
        choice= ask_choice()

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            year = int(input("Insert year: "))
            count = calculate_years(year, timestamps)
            print(f"Amount of timestamps during year {year} is {count}")
        elif choice == 2:
            month = input("Insert month: ")
            if month in MONTHS:
                count = calculate_months(month, timestamps)
                print(f"Amount of timestamps during month {month} is {count}")
            else:
                print("Invalid month.")
        elif choice == 3:
            weekday = input("Insert weekday: ")
            if weekday in WEEKDAYS:
                count = calculate_weekdays(weekday, timestamps)
                print(f"Amount of timestamps during weekday {weekday} is {count}")
        else:
            print("Invalid choice.")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
