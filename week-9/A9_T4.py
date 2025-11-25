TEMP_MIN = -273.15
TEMP_MAX = 10000

def collect_celsius():
    try:
        raw = input("Insert Celsius: ")
        celsius = float(raw)
        if celsius > TEMP_MAX or celsius < TEMP_MIN:
            print(f"{celsius} temperature out of range.")
            return None, False
        return celsius, True
    except ValueError:
        print(f"Could not convert string to float: '{raw}'")
        return None, False

def main():
    print("""
########################################################
# Task A9_T4
# Developer Enni Hirvonen
# Date 2025-11-25
########################################################""")
    print("Program starting.")

    temp_valid = False

    celsius, temp_valid = collect_celsius()

    if temp_valid == True:
        print(f"You inserted {celsius} °C")

    print("Program ending.")

if __name__ == "__main__":
    main()