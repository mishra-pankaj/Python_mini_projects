unit = input("Is this temperature in celcius or ferhenite(c/f): ")
temp = float(input("enter the temp : - "))

if unit == "c":
    temperature  = (9* temp)/5 + 32
    print(temperature)
elif unit == "f":
    ferehneite = (temp -32)* 5/9
else:
    print(f"{unit} is invalid")
