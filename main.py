import program
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation (sum, multiply, divide, subtract): ")
if operation == "sum":
    print(program.sum(a,b))
elif operation == "multiply":
    print(program.multiply(a,b))
elif operation == "divide":
    print(program.divide(a,b))
elif operation == "subtract":
    print(program.subtract(a,b))
else:
    print("Invalid operation")
