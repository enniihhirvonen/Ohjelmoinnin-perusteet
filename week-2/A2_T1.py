print("Program starting.")

Name=input("What is your name: ")

Feed=input("Enter a floating point number: ")
First=float(Feed)

Feed=input("Enter second floating point number: ")
Second=float(Feed)

print(Name, "you gave numbers", First, "and", Second)

Product=(First * Second)

print("Multiplying first and second number will result in product", round(Product, 2))

print("Program ending.")