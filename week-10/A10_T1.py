"""
########################################################
# Task A10_T1
# Developer Enni Hirvonen
# Date 2025-12-04
########################################################

"""

import sys

def read_file(filename, data):
    i = -1

    try:
        with open(f"week-10/{filename}", "r") as file:
            for line in file:
                i += 1
                if line.strip():
                    data[i] = line.strip()     
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

def print_data(data):
    print("# --- Vertically --- #")
    for value in data.values():
        print(value)
    print("# --- Vertically --- #")

    print("# --- Horizontally --- #")
    print(", ".join(data.values()))
    print("# --- Horizontally --- #")

def main():
    print("Program starting.")

    data = {}

    read_file(input("Insert filename: "), data)

    print_data(data)

    print("Program ending.")

if __name__ == "__main__":
    main()
