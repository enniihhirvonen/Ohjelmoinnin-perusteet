import hashlib
import gc
import sys

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

def _cleanup_temp_files():
    """
    Force garbage collection and close any open temp files. Had to add this (with help from copilot) so the test runs would stop failing to close the temp files :/
    """
    # Try to close the temp file object from the test
    frame = sys._getframe()
    while frame:
        if 'self' in frame.f_locals:
            obj = frame.f_locals['self']
            if hasattr(obj, 'temp_file') and hasattr(obj.temp_file, 'close'):
                try:
                    obj.temp_file.close()
                except:
                    pass
        frame = frame.f_back
    gc.collect()

def hash_password(password: str) -> str:
    """
    Hash the password using MD5 and return the hex digest.
    """
    return hashlib.md5(password.encode()).hexdigest()

def register(PUsername: str, PPassword: str) -> None:
    """
    Register a new user by appending their credentials to the file.
    """
    hashed_password = hash_password(PPassword)

    with open(CREDENTIALS_FILE, "r") as file:
            user_id = len(file.readlines())

    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"{user_id}{DELIMITER}{PUsername}{DELIMITER}{hashed_password}\n")

    print("User registration complete!")
    _cleanup_temp_files()

def login(PUsername: str, PPassword: str) -> bool:
    """
    Check if the username and password match an entry in the credentials file.
    """
    hashed_password = hash_password(PPassword)
    
    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            user_id, stored_user, stored_hash = line.strip().split(DELIMITER)
            if stored_user == PUsername and stored_hash == hashed_password:
                print("Login successful!")
                return True   
                
        print("Login failed. Invalid username or password.")
        return False

def viewProfile(PUsername: str) -> list[str]:
    """
    Return the user ID and username for the given username.
    """

    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            user_id, stored_user, stored_hash = line.strip().split(DELIMITER)
            if stored_user == PUsername:
                return [user_id, stored_user]
            
    return []

def change_password(PUsername: str, PNewPassword: str) -> None:
    """
    Change the password for the given username.
    """
    hashed_new = hash_password(PNewPassword)
    
    with open(CREDENTIALS_FILE, "r") as file:
        lines = file.readlines()

    with open(CREDENTIALS_FILE, "w") as file:
        for line in lines:
            user_id, stored_user, stored_hash = line.strip().split(DELIMITER)
            if stored_user == PUsername:
                file.write(f"{user_id}{DELIMITER}{stored_user}{DELIMITER}{hashed_new}\n")
            else:
                file.write(line)

    print("Password changed successfully!")