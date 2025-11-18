import time

def main():
    print("Program starting.")

    is_pause_duration = False

    while True:
        print("\nOptions:")
        print("1 - Set pause duration")
        print("2 - Activate pause")
        print("0 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            is_pause_duration = True
            pause_duration = float(input("Insert pause duration (s): "))
        elif choice == "2":
            if is_pause_duration == False:
                print("Pause is not set.")
            else:
                print(f"Pausing for {pause_duration} seconds.")
                time.sleep(pause_duration)
                print("Unpaused.")
        elif choice == "0":
            break
        else:
            print ("Invalid choice.")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()