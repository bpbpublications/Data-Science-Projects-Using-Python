try:
    age = int(input("Enter your age: "))
    if age <= 0:
        raise ValueError("Age must be greater than zero.")
except ValueError as e:
    print("Invalid input:", e)
else:
    print("Entered age value is correct:", age)
