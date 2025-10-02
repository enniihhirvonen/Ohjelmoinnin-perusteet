print("Program starting.\n")

Words=[]

while True:
    Word=input("Insert word (empty stops): ")
    if Word == "":
        break
    Words.append(Word) #adds inputted words into empty list

WordCount=len(Words)
CharCount=sum(len(Word) for Word in Words) #calculates length of each word in "Words" list and adds them all up

print("\nYou inserted:")
print(f"- {WordCount} words")
print(f"- {CharCount} characters")

print("\nProgram ending.")