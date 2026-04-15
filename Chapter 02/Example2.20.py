import random
# Random integer between two numbers
print(random.randint(20, 30))  # Random integer between 20 and 30
# Random floating-point number between 0 and 1
print(random.random())  # Random float between 0 and 1
# Random choice from a list
numbers = [12, 23, 34, 45, 56]
print(random.choice(numbers))  # Randomly selects a number from the list
# Shuffle a list
random.shuffle(numbers)  # Shuffle the list in place
print(numbers)
