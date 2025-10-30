import string
import os

def main():

    current_location, next_location, passphrase = progress()

    if next_location == 5:
        final_files()
        print("My journey is over.")
        return
    
    print("Travel starting.")

    locations = {
        0: "home",
        1: "Galba's palace",
        2: "Otho's palace",
        3: "Vitellius' palace",
        4: "Vespasian's palace"
    }
    
    print(f"Currently at {locations[int(current_location)]}.")

    print(f"Travelling to {locations[int(next_location)]}...")

    if next_location < 5:
        current_location += 1
        next_location += 1

    print(f"...Arriving to {locations[int(current_location)]}.")

    print("Passing the guard at the entrance.")
    print(f"\"{rot13(passphrase)}!\"")
    print("Looking for the message in the palace...\nAh, there it is! Seems cryptic.")

    passphrase = save_cipher(current_location)

    save_plain_message(current_location, passphrase)

    save_progress(current_location, next_location, passphrase)

    print("[Game] Progress autosaved!")

    print("Deciphering Emperor's message...")
    print("Looks like I've not got the plain version copy of the Emperor's message.")
    print("Time to leave...")

    print("Travel ending.")

def final_files(): # creates 2 files, one ciphered and one plain after all locations have been visited
    cipher_text = "Cneg 0 - Lrne bs gur Sbhe Rzcrebef:\nVa NQ 68, nsgre Areb'f qrngu, Ebzr cyhatrq vagb punbf\nJvgu ab pyrne urve, gur rzcver fnj encvq cbjre fgehttyrf.\nTnyon gbbx gur guebar svefg, sbyybjrq ol Bgub, Ivgryyvhf, naq svanyyl Irfcnfvna,\nrnpu onggyvat sbe pbageby va jung orpnzr gur Lrne bs gur Sbhe Rzcrebef."

    with open("final_cipher.txt", "w") as file:
        file.write(cipher_text)

    plain_text = rot13(cipher_text)

    with open("final_plain.txt", "w") as file:
        file.write(plain_text)

def save_cipher(current_location): # creates cipher file for each location
    passphrases = {
        1: "fgeratgu", # strength
        2: "ubabe", # honor
        3: "fgengrtl", # strategy
        4: "jrnygu" # wealth
    }

    with open(f"{current_location}_{passphrases[int(current_location)]}.gkg", "w") as file:
        file.write(f"{passphrases[int(current_location)]}")

    return passphrases[current_location]

def save_plain_message(current_location, passphrase): # creates plain text file for each location
   with open(f"{current_location}_{passphrase}.txt", "w") as txt:
        plain_passphrase = rot13(passphrase).strip()
        txt.write(plain_passphrase)

def save_progress(current_location, next_location, passphrase):
    with open("player_progress.txt", "a") as file:
        file.write(f"{current_location};{next_location};{passphrase}\n")

def rot13(passphrase): # ranslation function
    # found from stackoverflow :,)
    rot13 = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

    decipher = f"{passphrase}".translate(rot13)

    capital_decipher = str.capitalize(decipher)
    
    return capital_decipher

def progress(): # checks player progress
    if os.path.exists("player_progress.txt"): # if player_progress file exists, read the progress info
        with open("player_progress.txt", "r") as file:
            lines = file.readlines()
            last_progress = lines[-1].split(";")
            current_location = int(last_progress[0].strip())
            next_location = int(last_progress[1].strip())
            passphrase = (last_progress[2].strip())

    else: # if progress file doesnt exist, initialize it with starting values
        current_location = 0
        next_location = 1
        passphrase = "qvfpvcyvar"
        with open("player_progress.txt", "w") as file:
            file.write("current_location;next_location;passphrase\n")
            file.write("0;1;qvfpvcyvar\n")

    return current_location, next_location, passphrase

if __name__ == "__main__":
    main()