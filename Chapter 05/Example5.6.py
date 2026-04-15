# Base class (Parent class)
class Student1:
    def __init__(self, name, age):
        self.name = name  # Initializing the 'name' attribute
        self.age = age    # Initializing the 'age' attribute
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived class(Child class) inherits from Student1 class
class Student2(Student1):
    def __init__(self, name, age, regid):
        # Calling the constructor of the parent class (Student1)
        super().__init__(name, age)
# Initializing the 'regid' attribute specific to Student2 class
        self.regid = regid  
    
    def display_details(self):
        self.display()  # Calling the display method of the parent class
        print(f"RegId: {self.regid}")

# Creating an object of the derived class (child class)
s2 = Student2("Sunil", 20, 101)
# Accessing the methods and attributes
s2.display_details()  
# Output: Name: Sunil, Age: 20, RegId: 101
