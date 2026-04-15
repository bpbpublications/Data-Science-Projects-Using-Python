def calc(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "division":
        return a/b
    elif operation == "multiply":
        return a*b
    else:
        return "Invalid operation"

print("Result after addition is:",calc(10, 5, "add"))
print("Result after subtraction is:",calc(10, 5, "subtract"))
print("Result after division is:",calc(10, 5, "division"))
print("Result after multiplication is:",calc(10, 5, "multiply"))
