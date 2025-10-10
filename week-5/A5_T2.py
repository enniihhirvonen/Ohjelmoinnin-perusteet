def main():
    print("Program starting.\n")
    pword=input("Insert word: ")
    frameword(pword)
    print("\nProgram ending.")
    return None

def frameword(pword):
    length=(len(pword) + 4)
    print('*' * length)
    print(f"* {pword} *")
    print('*' * length)
    return None

main()

