def main():
    print("Program starting.\n")
    pname=askname()
    greetuser(pname)
    print("\nProgram ending.")

def askname():
    name=input("What is your name? ")
    return name

def greetuser(pname):
    print(f"Hello, {pname}!")
    return None

main()