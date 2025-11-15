"""
NEEDED FUNCTIONS:
    main for logic and probably input for filename and plugs
    word input, rotor scramble (could be a function/functions inside a function), word output
        LOOP this so user can keep inserting words for as long as they dont press enter/write an empty row
        REMEMBER to reset the positions of the rotors after each input in order to allow for accurate encryption/decryption.

"""

# im gonna crash out why is it not working AAAAAAAAAAAA

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def read_file(filename, rotors):
    reflector = ""

    with open(f"week-7/txt/{filename}", "r") as file:
        for line in file:
            line = line.strip()
            label, scramble = line.split(":", 1)
            if label.startswith("Rotor"):
                rotors[label] = list(scramble)
            elif label.startswith("Reflector"):
                reflector = scramble

    return reflector

def scramble_row(row, rotors, reflector):
    rotor_pos = [0, 0, 0]
    result = []

    for char in row:
        if char not in alphabet:
            continue
        rotate_positions(rotor_pos)
        fwd = forward_pass(char, rotors, rotor_pos)
        ref = reflector_pass(fwd, reflector)
        rev = reverse_pass(ref, rotors, rotor_pos)
        print(f"Character \"{char}\" illuminated as \"{rev}\"")
        result.append(rev)

    print(f"Converted row - \"{"".join(result)}\".")

    return None

def rotate_positions(rotor_pos):
    rotor_pos[0] = (rotor_pos[0] + 1) % 26 # moves rotor 1
    if rotor_pos[0] == 0: # checks if rotor 1 has moved a full rotation back to 0
        rotor_pos[1] = (rotor_pos[1] + 1) % 26 # does the same stuff for rotor 2
        if rotor_pos[1] == 0:
            rotor_pos[2] = (rotor_pos[2] + 1) % 26 # does the same stuff for rotor 3

def forward_pass(char, rotors, rotor_pos):
    idx = alphabet.index(char) 
    for i in range(3): # loops through each rotor
        idx = (idx + rotor_pos[i]) % 26 # adjusts index based on rotor position
        char = rotors[f"Rotor{i + 1}"][idx] # gets the scrambled character from the rotor
        idx = alphabet.index(char) # updates index for next rotor

    return char

def reflector_pass(char, reflector):
    idx = alphabet.index(char)
    char = reflector[idx] # gets the opposite character from reflector (eg. A > Y > A)

    return char

def reverse_pass(char, rotors, rotor_pos):
    idx = alphabet.index(char)
    for i in reversed(range(3)):
        idx = (idx + rotor_pos[i]) % 26 # same as forward_pass
        char = alphabet[idx]
        idx = rotors[f"Rotor{i+1}"].index(char) # gets the index where current char is in rotor
        
    return char

def main():
    filename = input("Insert config (filename): ")

    while True:
        plugs = input("Insert plugs (y/n)?: ")
        if plugs == "n":
            print("No extra plugs inserted.")
            break
        elif plugs == "y":
            print("This feature has not been implemented yet.")
            break
        else:
            print("Invalid answer, try again.")

    rotors = {}

    reflector = read_file(filename, rotors)

    print("Enigma initialized.")

    while True:
        row = input("Insert row (empty stops): ")
        if row == "":
            print("Enigma closing.")
            break
        scramble_row(row, rotors, reflector)

if __name__ == "__main__":
    main()