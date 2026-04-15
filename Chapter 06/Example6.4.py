import mysql.connector
# MySQL Database Connection Configuration
conn=mysql.connector.connect(
	    host="localhost",
	    user="root",
	    password="sasml",
	    database="student"
	)
# Cursor object and Connection interaction
cursor = conn.cursor()
# Executing SQL Query to update a record into table 'student_tbl'
cursor.execute("""UPDATE student_tbl SET first_name = 'Ajay',
	                last_name='Singh',course='Java'
	               where studentid = 101""")
# fetch all the records in a table using fetchall() 
display = cursor.fetchall()
conn.commit()
cursor.execute("""SELECT * FROM student_tbl 
	                where studentid = 101""")
display_record = cursor.fetchall()
# fetch the records using loops and display using '\n'
for x in display_record:
    print(x,'\n')
# Changes are commit to the database
conn.commit()
# Close the cursor and connection
cursor.close()
conn.close()
