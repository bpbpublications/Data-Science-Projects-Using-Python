import re

email = input("Enter your email id")
# Search for an email pattern
email_check = r'\w+@\w+\.\w+'
email_match = re.search(email_check, email)

if email_match:
    print("Entered Email is correct:", email_match.group())
else:
    print("Entered Email is not correct")
