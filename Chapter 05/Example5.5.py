# Defining a class with a constructor
class Course:
    def __init__(self,course_name,course_duration):
        self.course_name = course_name #Initializing the 'course_name' attribute
        self.course_duration =course_duration #Initializing the 'course_duration' attribute

    def display_details(self):
        print(f"Course Name: {self.course_name}, Duration: {self.course_duration}")

# Creating an object of the Course class
course1 = Course("Python","1 Month")
# Accessing method to display details
course1.display_details()  
