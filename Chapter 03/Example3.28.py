def display_numbers():
    yield 1
    yield 2
    yield 3

for num in display_numbers():
    print(num)
