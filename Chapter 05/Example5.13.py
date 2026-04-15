import re

input_text = "Python is a language for Data Science."
string_pattern = r"language"

if re.search(string_pattern, input_text):
    print("Yes, 'language' is in the given text.")
else:
    print("No, word is not found.")
