import sys

def main():
    print("""
########################################################
# Task A9_T2
# Developer Enni Hirvonen
# Date 2025-11-25
########################################################""")
    
    print("\nProgram starting.")

    code = int(input("\nInsert exit code (0-255: )"))

    if code == 0:
        print("Clean exit")
    else:
        print("Error code\n")
    sys.exit(code)

if __name__ == "__main__":
    main()