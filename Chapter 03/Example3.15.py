marks = [82,74,91,82,92]
#start at index 4,go up to index 1 but not including index 1
#Step -1  move in reverse
print(marks[4])#Output:92
print(marks[4:1:-1])#Output:[92, 82, 91]
print(marks[4:0:-1])#Output:[92, 82, 91, 74]
