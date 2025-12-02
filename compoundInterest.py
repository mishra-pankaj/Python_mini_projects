principle = float(input("Enter you Priniciple Amount:- "))
rate = float(input("Enter the rate of Interset:- "))
time = float(input("Enter your time period in Y: "))

amount = principle * pow((1+ rate/100)*time)
print(f"Your final amount will be {amount}")
