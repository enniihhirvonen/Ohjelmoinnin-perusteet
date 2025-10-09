print("Program starting.")

Value=int(input("Insert a positive integer: "))

Values=[]

while (Value != 1):
    Values.append(Value) #adds new value to list

    if (Value % 2 == 0): #check even
        Value=int(Value // 2)
    else: #check odd
        Value=int(Value * 3 + 1)

Values.append(Value) #adds final value, which is always 1)

print(*Values, sep=" -> ") #asterisk stops list from printing with brackets around it

print(f"Sequence had {len(Values) - 1} total steps.") # -1 removes the final "1" from the end of the list

print("\nProgram ending.")