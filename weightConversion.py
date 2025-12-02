weight = float(input("Enter your weight:- "))
unit =input("kilogram or pound? (K or L): ")

if unit == "k":
    Pound_conversion = weight* 2.205
    print(f"Your Weight {weight} kg in pound is {Pound_conversion} ")

elif unit == "L":
    Kilogram_conversion = weight /2.205
    print(f"Your Pound {weight} lb in kilogram  is {Kilogram_conversion}")

else :
    print(f"{unit} is invalid")