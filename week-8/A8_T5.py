# had to revise all of this code for the classroom test but im keeping all of this as is bc im too tired

import hashlib

CREDENTIALS_FILE = "credentials.txt"

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def show_options(user_loggedin):
    if user_loggedin == False:
        print("\nOptions:")
        print("1 - Login")
        print("2 - Register")
        print("0 - Exit")
    else:
        print("\nUser menu:")
        print("1 - View profile")
        print("2 - Change password")
        print("0 - Log out")

    return None

def ask_choice():
    return int(input("Your choice: "))

def login():
    username = input("Insert username: ")
    password = input("Insert password: ")

    hashed_password = hash_password(password)

    with open(f"week-8/txt/{CREDENTIALS_FILE}", "r") as file:
        for line in file:
            user_id, stored_user, stored_hash = line.strip().split(";")
            if stored_user == username and stored_hash == hashed_password:
                print("Login successful!")
                return True, (user_id, stored_user)
    
        print("Login failed. Invalid username or password.")
        return False, None

def register():
    username = input("Insert username: ")
    password = input("Insert password: ")

    hashed_password = hash_password(password)

    with open(f"week-8/txt/{CREDENTIALS_FILE}", "r") as file:
        user_id = len(file.readlines())

    with open(f"week-8/txt/{CREDENTIALS_FILE}", "a") as file:
        file.write(f"{user_id};{username};{hashed_password}\n")

    print("User registration complete!")

def view_profile(user_data):
    user_id, username = user_data
    print(f"User ID: {user_id}")
    print(f"Username: {username}")

def make_choice(choice, user_loggedin, user_data):
    if user_loggedin == False:
        if choice == 1:
            success, data = login()
            if success:
                return True, data
        elif choice == 2:
            register()
    else:
        if choice == 1:
            view_profile(user_data)
        elif choice == 2:
            print("This option hasn't been implemented yet.")
    
    return user_loggedin, user_data

def main():
    print("Program starting.")

    user_loggedin = False
    user_data = None

    while True:
        show_options(user_loggedin)

        choice = ask_choice()

        if choice == 0 and user_loggedin == False:
            print("Exiting program.")
            break
        elif choice == 0 and user_loggedin == True:
            print("Logging out...")
            user_loggedin = False
            user_data = None
        else: 
            user_loggedin, user_data = make_choice(choice, user_loggedin, user_data)


    print("\nProgram ending.")

    return None

if __name__ == "__main__":
    main()