operator = input("Enter an operator(+ - / *): ")
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
if operator == "+":
    sum = number1+number2
    print(round(sum,3))
elif operator == "-":
    dif = number1-number2
    print(dif)
elif operator == "*":
    pro = number1*number2
    print(pro)
elif operator == "/":
    div = number1/number2
    print(div)
else:
    print(f"Enter A valid{operator}")