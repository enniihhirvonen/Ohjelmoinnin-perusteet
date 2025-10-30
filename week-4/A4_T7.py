#tää ei nyt millään mee läpi testistä vaikka se toimii kuitenkin................ en tiedä mikä ongelma. kun vaihtaa test_main.py "python3" --> "python" toimii täydellisesti, mutta en viitsi classroomissa vaihdella testin koodia

print("Program starting.\n")

print("Check multiplicative persistence.")

Value=input("Insert an integer: ")

Steps=0 #step counter

while len(Value) > 1:
    Product = 1 #"Product" variable stores multiplication product
    Steps += 1 #"Steps" variable increases by 1 every loop
    StepString = "" #"Stepstring" variable stores each "Character" from Value

    for Character in Value: #loop continues for each Character in Value
        Digit = int(Character) #converts string into integer to allow multiplication
        Product *= Digit
        StepString += (Character + " * ") #adds asterisk inbetween each Character

    print(f"{StepString[:-3]} = {Product}") #[:-3] removes last three characters from "Stepstring" which is the last " * "]

    Value = str(Product) #converts Value back to string to allow loop to continue

print("No more steps.\n")

print(f"This program took {Steps} step(s)")

print("\nProgram ending.")