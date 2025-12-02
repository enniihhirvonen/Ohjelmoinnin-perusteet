def askIntByte(PPrompt: str) -> int:
    # Ask for input
    Feed = input(PPrompt)

    # TODO: Use try-except to:
    #   - Convert input to float and int  

    try:
        #   - Raise an exception if input is not numeric
        if Feed.isnumeric() == False:
            print(f'"{Feed}" is non-numeric value.')
            raise ValueError

        value_float = float(Feed)

        #   - Raise an exception if input is not an integer
        if value_float.is_integer() == False:
            print(f'"{Feed}" is non-numeric value.')
            raise ValueError
    
        value_int = int(Feed)

        #   - Raise an exception if input is not in the range 0–255
        if value_int < 0 or value_int > 255:
            print(f'Value "{Feed}" is out of the range 0-255.')
            raise ValueError
        
        # If all checks pass, return the integer value
        return value_int
        
    except Exception:
        raise

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    # TODO: Return a hex string in the format "#rrggbb"
    # Use string formatting: "{:02x}"
    return "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)

def main():
    print("Program starting.")

    try:
        #   - Call askIntByte for red, green, and blue
        red = askIntByte("Insert red: ")
        green = askIntByte("Insert green: ")
        blue = askIntByte("Insert blue: ")

        #   - Call createHex to get the hex color
        hex_color = createHex(red, green, blue)

        #   - Print RGB values, hex value, and binary (8-bit) values
        print("RGB Details:")
        print(f"- Red: {red}")
        print(f"- Green: {green}")
        print(f"- Blue: {blue}")
        print(f"Hex: {hex_color}")
        print(f"Binary:")
        print(f"- Red: {red:08b}")
        print(f"- Green: {green:08b}")
        print(f"- Blue: {blue:08b}")

    #   - If any exception occurs, print the error and a message like:
    #     "Couldn't perform the designed task due to the invalid input values."
    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")

if __name__ == "__main__":
    main()