# Defining a class with a constructor
class Student:
    def __init__(self, name, rollno):
        self.name = name  # Initializing the 'name' attribute
        self.rollno = rollno  # Initializing the 'rollno' attribute
    def display(self):
        print(f"Student Name: {self.name}, RollNo: {self.rollno}")
# Creating objects
student1 = Student("ABC", 101)
# Accessing attributes and methods
student1.display() #Output: Student Name: ABC, RollNo: 101
