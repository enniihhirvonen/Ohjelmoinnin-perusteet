""""
NEEDED FUNCTIONS
main for logic, input
read file, split lines by delimiter ";"
results
"""

from collections import namedtuple

TIMESTAMP = namedtuple("TIMESTAMP", ["weekday", "hour", "consumption", "price", "total"])

def readTimestamps(filename, timestamps):
    with open(f"week-7/csv/{filename}", "r") as file:
        next(file)
        for line in file:
            if line.strip():
                parts = line.strip().split(";")
                weekday = parts[0]
                hour = float(parts[1])
                consumption = float(parts[2])
                price = float(parts[3])
                total = round(consumption * price, 2)
                timestamps.append(TIMESTAMP(weekday, hour, consumption, price, total))

    return None

# def analyseTimestamps(timestamps, results):

#     for timestamp in timestamps:
#         result = []

#         weekday = timestamp[0]
#         result.append(weekday)

#         hour = float(timestamp[1])
#         result.append(f"{hour:.2f}")

#         consumption = float(timestamp[2])
#         result.append(f"{consumption:.2f}")

#         hourly_price = float(timestamp[3])
#         result.append(hourly_price)

#         total_price = round(consumption * hourly_price, 2)
#         total_price = str(total_price)
#         result.append(total_price)

#         print(f"Result after processing: {result}")

#         results.append(result)

#     return None

def displayTimestamps(timestamps):
    print("Electricity usage:")

    for ts in timestamps:
        print(f" - {ts.weekday} {ts.hour:.2f}, price {ts.price}, consumption {ts.consumption:.2f} kWh, total {ts.total} €")

    return None
    
def main():
    print("Program starting.")

    timestamps = []
    results = []

    filename = input("Insert filename: ")

    print(f"Reading file \"{filename}\".")

    readTimestamps(filename, timestamps)

    # analyseTimestamps(timestamps, results)

    displayTimestamps(timestamps)

    print("Program ending.")

if __name__ == "__main__":
    main()