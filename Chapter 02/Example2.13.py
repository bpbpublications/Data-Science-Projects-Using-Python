x = 12  # Global variable
def display():
    y = 3  # Local variable
    print("Value of x Inside function: x =",x)
    print("Value of y Inside function: y =",y)
display()
print("Printing x Outside function: x =", x)
# This would cause an error, variable 'y’ falls outside its scope
# print("Printing y Outside function: y =", y)  
