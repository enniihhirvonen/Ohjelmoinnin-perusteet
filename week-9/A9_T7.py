import sys
import os

def showHelp() -> None:
    print("[USAGE] python A9_T7.py src_file dst_file")

def copyFile(PSrcFile: str, PDstFile: str) -> None:
    Proceed = True
    if (os.path.exists(PDstFile)):
        print(f'Destination file "{PDstFile}" already exists.')
        answer = input("Do you want to overwrite it? (y/n): ")
        if answer != "y":
            Proceed = False
    if Proceed:
        try:
            with open(PSrcFile, "r") as src:
                content = src.read()
            with open(PDstFile, "w") as dst:
                dst.write(content)
            print(f'Copying file "{PSrcFile}" to "{PDstFile}".')
        except Exception:
            print(f"Couldn't copy \"{PSrcFile}\" to \"{PDstFile}\"")
            sys.exit(-1)

def main() -> None:
    print("""
########################################################
# Task A9_T7
# Developer Enni Hirvonen
# Date 2025-12-03
########################################################""")
    
    print("Program starting.")

    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        showHelp()
        sys.exit(-1)

    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    copyFile(src_file, dst_file)

    print("Program ending.")

if __name__ == "__main__":
    main()