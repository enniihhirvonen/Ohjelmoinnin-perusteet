"""
NEEDED FUNCTIONS
    main for logic and input
    read file
    timestamp analysis
    display results

Preferred datastructures:
    Timestamps: list[TIMESTAMP]
    Analysis helper: list[DAY_USAGE]
    Results: list[str]

"""

from dataclasses import dataclass

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday") # i just noticed saturday is misspelled (╥﹏╥)

def read_timestamps(filename, timestamps, TIMESTAMP):
    with open(filename, "r") as file:
        next(file)
        for line in file:
            if line.strip():
                parts = line.strip().split(";")
                weekday = parts[0]
                hour = float(parts[1])
                consumption = float(parts[2])
                price = float(parts[3])
                total = consumption * price
                ts = TIMESTAMP(weekday, hour, consumption, price, total)
                timestamps.append(ts)

    return None
    
def analyse_timestamps(timestamps, DAY_USAGE, results):
    daily = {day: DAY_USAGE(day, 0.0, 0.0) for day in WEEKDAYS} # initalize gatherer variables for each day

    for ts in timestamps:
        daily[ts.weekday].usage += ts.consumption
        daily[ts.weekday].cost += ts.total

    for day in WEEKDAYS:
        results.append(daily[day])

    return None
        
def display_results(results):
    print("### Electricity consumption summary ###")

    for day in results:
        print(f" - {day.weekday} usage {day.usage:.2f} kWh, cost {day.cost:.2f} €")

    print("### Electricity consumption summary ###")

def main():
    # initalize classes and lists first
    @dataclass
    class TIMESTAMP:
        weekday: str
        hour: float
        consumption: float
        price: float
        total: float

    @dataclass
    class DAY_USAGE:
        weekday: str
        usage: float
        cost: float
        
    timestamps = []
    results = []

    print("Program starting.")
    
    filename = input("Insert filename: ")

    print(f"Reading file \"{filename}\".")

    read_timestamps(filename, timestamps, TIMESTAMP)

    print("Analysing timestamps.")

    analyse_timestamps(timestamps, DAY_USAGE, results)

    print("Displaying results.")

    display_results(results)

    print("Program ending.")

if __name__ == "__main__":
    main()