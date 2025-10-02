print("Welcome to the temp app!")
Temp=int(input("What is the temperature of CPU? "))

if(Temp > 80):
    print("Warning, temperature too high!")

elif(Temp < 80):
    print("All cool, keep on going!")

print("Checking temperature parity...")

if(Temp % 2 == 0):
    print("Number is even.")

else:
    print("Number is odd.")

#2

Name1=input("First name: ")
Name2=input("Second name: ")

if len(Name1) > len(Name2):
    print("First name is longer than second name.")

elif len(Name1) < len(Name2):
    print("Second name is longer than first name.")

elif len(Name1) == len(Name2):
    print("Both names are the same length.")

#3

import random

print(random.random())
print(random.randint(1, 10))

Player=input("Choose rock, paper or scissors: ")
print("Rock, paper, scissors, shoot! ")

choices=["rock", "paper", "scissors"]

Computer=(random.choice(choices))

print(f"You chose {Player}")
print(f"Computer chose {Computer}")

if Player == Computer:
    print("It's a tie!")

elif (Player == "rock" and Computer == "scissors") or (Player == "scissors" and Computer == "paper") or (Player == "paper" and Computer == "rock"):
    print("You win!")

else:
    print("Computer wins!")
