var1=["python","java"]
var2=["python","java"]
var3=var1
print(var1 is var3) # Output:True(var3 is the same object as var1)
print(var1 is var2) # Output:False(var1 and var2 are different objects)
print(var1==var2)   # Output:True(var1 and var2 have the same content)
