print("Program starting.")

Word=input("Insert a closed compound word: ")
Reverse=Word[::-1]
Length=len(Word)
Length=str(Length)
LastChar=Word[-1]

print("The word you inserted is \'" + Word + "\' and in reverse it is \'" + Reverse + "\'.")
print("The inserted word length is " + Length)
print("Last character is \'" + LastChar + "\'")

print("Take substring from the inserted word by inserting...")
start=int(input("1) Starting point: "))
end=int(input("2) Ending point: "))
step=int(input("3) Step size: "))

Substring=Word[start:end:step]
print("The word \'" + Word + "\' sliced to the defined substring is \'" + Substring + "\'.")

print("Program ending.")