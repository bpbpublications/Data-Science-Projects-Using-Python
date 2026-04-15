import mysql.connector
# MySQL Database Connection Configuration
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sasml",
    database="student"
)
# Cursor object and Connection interaction
cursor = conn.cursor()
# Taking input from user
studentid = int(input("Enter Student ID: "))
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
course = input("Enter Course Name: ")
# Executing SQL Query with placeholders to insert a record
query = """INSERT INTO student_tbl(studentid,first_name,last_name,course) 
           VALUES (%s, %s, %s, %s)"""
values = (studentid,first_name,last_name,course)
cursor.execute(query, values)
# Committing the changes
conn.commit()
# Closing the cursor and connection
cursor.close()
conn.close()
print("Record inserted successfully.")

