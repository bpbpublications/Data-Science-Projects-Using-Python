# Parent class
class Coursedetail:
    def __init__(self,duration,fees):
        self.duration = duration
        self.fees = fees

    def displaydetail(self):
        print(self.duration,"is the duration and",self.fees,"is the fees of the course.")

# Child class(Subclass)
class Coursename(Coursedetail):
    def __init__(self, name):
        self.name = name

    def displaydetail(self):
        print(self.name,"is the name of the course.")

# Creating objects
C1 = Coursename("Php") # ‘C1’ is the object of Coursename class
C2 = Coursedetail("4 weeks", 4000) # ‘C2’ is the object of Coursedetail class

# Method overriding in action
C1.displaydetail()
C2.displaydetail()
