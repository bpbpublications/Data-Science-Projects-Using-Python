class Student:
    def __init__(self,name,marks):
        self.__name = name   # private attribute
        self.__marks = marks # private attribute

    # Method to display the data
    def display_details(self):
        print("Student Name is:", self.__name)
        print("Student Marks is:", self.__marks)
    # Method to change marks
    def updatename(self, update_name):
        self.__name = update_name
# Create object of Student
s1=Student("Anil",76)
# Accessing data using method 'display_details()'
s1.display_details()
# Changing marks using method 'updatename()'
s1.updatename("Anil Kumar")
# Display updated data
s1.display_details()
