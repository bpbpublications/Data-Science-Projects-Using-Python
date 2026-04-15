# Define a class named Calculator
class Calc:
    # A method to add two numbers
    def addition(self,a,b):
        return a + b
    # A method to subtract two numbers
    def subtraction(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a*b

# Create an object of the Calculator class
calc1 = Calc()
# Call the add method
result1 = calc1.addition(25,20)
print("Addition of two numbers:",result1) # Output:45
# Call the subtract method
result2 = calc1.subtraction(25,20)
print("Subtraction:", result2) # Output:5
result3=calc1.multiply(2,3)
print("Multiplication:",result3)#Output:6
