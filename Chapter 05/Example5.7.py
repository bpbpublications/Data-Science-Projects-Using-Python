class Calc:
    def addition(self,a,b=0,c=0):
        return a+b+c

calc1 = Calc() #calc1 is object of class Calc
print("One Parameter:",calc1.addition(15))# Output:15
print("Two Parameter:",calc1.addition(15,10))  # Output: 25
print("Three Parameter:",calc1.addition(15,10,5))# Output: 30
