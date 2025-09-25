print("Program starting.")

feed=input("Insert fahrenheits: ")

fahrenheit=round(float(feed), 1)
celsius=round((fahrenheit - 32)/1.8, 1)

print(fahrenheit, "°F is", celsius, "°C")

print("Program ending.")