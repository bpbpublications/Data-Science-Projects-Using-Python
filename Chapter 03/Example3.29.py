def display_even_numbers(number):
    for n in number:
        if n % 2 == 0:
            yield n

nums = [8, 15, 32, 37, 50]
for even in display_even_numbers(nums):
    print(even,"is even number")
