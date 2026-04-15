class Calculator:
    def compute(self):
        pass  # Placeholder for specific operations
# Derived Class for Add
class Add(Calculator):
    def compute(self, a, b):
        return a + b
# Derived Class for Subtraction
class Subtract(Calculator):
    def compute(self, a, b):
        return a - b
# Using the classes
add = Add()
subtract = Subtract()
print("Addition:", add.compute(15, 10))      # Output: 25
print("Subtraction:", subtract.compute(20, 15))  # Output: 5
