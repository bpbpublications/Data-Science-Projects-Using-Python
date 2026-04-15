import re
mobile_number = input("Enter your mobile number: ")
# Pattern to match exactly 10 digits only
pattern = r"^\d{10}$"
if not re.match(r"^\d+$", mobile_number):
    print("Error: Mobile number must contain only digits.")
elif not re.match(pattern, mobile_number):
    print("Error: Mobile number must be exactly 10 digits long.")
else:
    print("Entered number is correct")
