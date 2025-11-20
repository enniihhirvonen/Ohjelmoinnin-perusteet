from loginLib import login, register, viewProfile, change_password

def main() -> None:
    print("Program starting.")
    mainMenu()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def mainMenu() -> None:
    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            username = askValue("username")
            password = askValue("password")
            if login(username, password):
                userMenu(username)
        elif choice == 2:
            username = askValue("username")
            password = askValue("password")
            register(username, password)
        elif choice == 0:
            break

def userMenu(PUsername: str) -> None:
    while True:
        showUserMenu()
        choice = askChoice()

        if choice == 1:
            profile = viewProfile(PUsername)
            if profile:
                print(f"User ID: {profile[0]}")
                print(f"Username: {profile[1]}")
        elif choice == 2:
            new_pass = askValue("new password")
            change_password(PUsername, new_pass)
        elif choice == 0:
            print("Logging out...")
            break

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> str:
    return input(f"Insert {PPrompt}: ")

if __name__ == "__main__":
    main()