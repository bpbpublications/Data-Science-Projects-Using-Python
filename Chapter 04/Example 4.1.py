try:
    num = int(input("Enter a number: "))
    result = 10/num
    print("Result is:", result)
except ZeroDivisionError:
    print("Error: You are dividing a number by zero.")
except ValueError:
    print("Error: Please enter a valid number.")
else:
    print("The input provided is Ok.")
finally:
    print("Thank you!")
