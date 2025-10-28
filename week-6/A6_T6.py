LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

"""NEEDED FUNCTIONS:
    shiftCharacter(character, alphabet)
    rot13(text)
    writeFile(filename, content)
    """

def main():
    print("Program starting.")
    print("Collecting plain text rows for ciphering.")

    text = []

    while True:
        line = input("Insert row(empty stops): ")
        if line == "":
            break
        text.append(line)

    content = rot13(text) # ciphers text for later use

    print("Options:")
    print("1 - Print ciphered text")
    print("2 - Save ciphered text to file")

    choice = input("Your choice: ")

    if choice == "1":
        print("#### Ciphered text ####")
        print(content) # prints the return value from rot13 function
 
    elif choice == "2":
        print("#### Ciphered text ####")
        filename = input("Insert filename to save: ")
        writeFile(filename, content)
        print("Ciphered text saved!")

    print("Program ending.")

def rot13(text):
    # was having difficulty with test_main.py inputs being a list of strings instead of one string or something ?? so this makes sure that the output for the test is correct by checking if text is in string form and then converting it to a list
    if isinstance(text, str): 
        text = [text] 

    content = []

    for line in text:
        newLine = ""
        for char in line:
            if char in LOWER_ALPHABETS:
                newChar = shiftCharacter(char, LOWER_ALPHABETS)
                newLine += newChar #shifts lowercase characters and adds to newLine string
            elif char in UPPER_ALPHABETS:
                newChar = shiftCharacter(char, UPPER_ALPHABETS)
                newLine += newChar # shifts uppercase characters and adds to newLine string
            else:
                newLine += char # if character isnt in either alphabet, adds it to newLine as is
        content.append(newLine)

    return "\n".join(content) # joins lines into a single string

def shiftCharacter(char, alphabet):
    if char in alphabet:
        return alphabet[(alphabet.index(char) + 13) % 26] #shifts characters using indexing
    return char

def writeFile(filename, content):
    with open(filename, "w", encoding='UTF-8') as file:
        file.write(content)

if __name__ == "__main__":
    main()