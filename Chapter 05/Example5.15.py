import re
input_name = input("Enter your name: ")
# Pattern to match only alphabets(uppercase and lowercase),minimum 1 character
pattern = r"^[A-Za-z]+$"
if re.match(pattern,input_name):
    print("Welcome.",input_name)
else:
    print("Invalid input:Only alphabetic characters are allowed")
