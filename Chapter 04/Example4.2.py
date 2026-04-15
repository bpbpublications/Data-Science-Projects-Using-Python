try:
    mob_no = int(input("Enter your mobile number: "))
    print("You entered mobile number:", mob_no)
except ValueError:
    print("Error: Please enter a valid number.")
