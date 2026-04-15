age = int(input('Enter your age'))
if age<=10:
    print("You are a child.")
elif 11<=age<=18:
    print("You are eligible for voting.")
elif 19<=age<65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
