student = {
	    'name': 'Anil',
	    'age': 34,
	    'courses': ['Python', 'AI']
	}
print(student['name'])  # Output: Anil
print(student['age'])   # Output: 34
	
student['age']=35
student['semester']='Fifth'
print(student['semester'])# Output: Fifth
print(student['age'])     # Output: 35
student.pop('age') #Removes an item by key
del student['courses'] #Removes an item or the entire dictionary
	
for key, value in student.items():
   print(key, value)  # Only prints name and semester
