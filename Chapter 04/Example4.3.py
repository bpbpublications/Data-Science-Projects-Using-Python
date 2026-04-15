try:
    name = input("Enter your name (strings only): ")
    if name.isdigit():
        raise ValueError("Numbers are not allowed as a name.")
    print("Welcome,", name)
except ValueError as e:
    print("Error:", e)
