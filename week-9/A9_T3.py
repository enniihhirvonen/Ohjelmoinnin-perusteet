def read_file(filename, text):
    try:
        with open(f"week-9/txt/{filename}", "r") as file:
            for line in file:
                text.append(line.strip())
            return True
    except FileNotFoundError:
        print(f"Couldn't read file \"{filename}\"")
        print()
        return False

def print_file(text, filename):
    print(f"## {filename} ##")
    for line in text:
        print(line)
    print(f"## {filename} ##")

def main():
    print("""
########################################################
# Task A9_T3
# Developer Enni Hirvonen
# Date 2025-11-25
########################################################""")
    
    file_exists = False
    text = []

    print("\nProgram starting.")

    filename = input("\nInsert filename: ")

    file_exists = read_file(filename, text)

    if file_exists == True:
        print_file(text, filename)
    else: 
        return
    
    print("\nProgram ending.")

if __name__ == "__main__":
    main()