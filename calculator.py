# Simple Calculator

a = int(input("Enter the first number: "))
op = input("Choose an operation (+, -, *, %, //): ")
b = int(input("Enter the second number: "))

# Here Apply Logic
if op == "+":
    print(f"Result: {a} + {b} = {a + b}")
elif op == "-":
    print(f"Result: {a} - {b} = {a - b}")
elif op == "*":
    print(f"Result: {a} * {b} = {a * b}")
elif op == "%":
    print(f"Result: {a} % {b} = {a % b}")
elif op == "//":
    print(f"Result: {a} // {b} = {a // b}")
else:
    print("Invalid operator! Please use one of (+, -, *, %, //).")
