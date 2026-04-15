# Defining a class
class Student:
    # Constructor to initialize attributes
    def __init__(self, cname, cduration):
        self.cname = cname         # Attribute
        self.cduration = cduration # Attribute
    
    # Method to display details
    def display(self):
        print(f"CourseName: {self.cname}, CourseDuration: {self.cduration}")
# Creating objects (instances of the class)
student1 = Student("Java", "One Month")  # Object1
student2 = Student("Python", "One Month") # Object2
# Accessing attributes and methods
student1.display() #Output: CourseName: Java,CourseDuration:One Month
student2.display() #Output: CourseName: Python,CourseDuration:One Month
