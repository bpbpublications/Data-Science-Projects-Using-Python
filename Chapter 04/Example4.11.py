# Read existing content from the file
try:
    with open("c:\\test.txt", "r") as file:
        content = file.read()
        print("Original Content in file:\n", content)
except FileNotFoundError:
    print("File not found. Creating a new one.")

# Append new content to the file using append mode 'a'
with open("c:\\test.txt", "a") as file:
    file.write("\nThis is new content added after reading.")
    print("New content has been added.")
