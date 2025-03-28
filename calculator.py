# simple-calculator 
a = int(input("type 1st value : "))
b = int(input("type 2nd value : "))
c = input("What operation do you want (+, -, *, %, //): ")

if c == "+":
    print(f"result : {a} + {b} = {a+b}")
elif c == "-":
    print(f"result : {a} - {b} = {a-b}")
elif c == "*":
    print(f"result : {a} * {b} = {a*b}")
elif c == "%":
    print(f"result : {a} % {b} = {a%b}")
elif c == "//":
    print(f"result : {a} // {b} = {a//b}")
else:
    print(f"Invalid operator plz enter one of +, -, *, %, //")