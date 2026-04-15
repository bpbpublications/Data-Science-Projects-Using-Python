courses = ['Python','Java','DotNet']
courses.append('C++') #Added one more item.
print(courses)  # Output: ‘Python’,‘Java’,‘DotNet’,‘C++’
courses.remove('Java') #remove the item.
print(courses)  # Output: ‘Python’,‘DotNet’,‘C++’
courses.pop(0)  # remove item at 0th position.
print(courses)  # Output:‘DotNet’,‘C++’
