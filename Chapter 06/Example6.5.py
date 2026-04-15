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
# Executing SQL Query to delete a record from table 'student_tbl'
cursor.execute("""DELETE FROM student_tbl WHERE studentid = 101""")
print("Record deleted successfully.\n")
# Commit the deletion to the database
conn.commit()
# Display the remaining records
cursor.execute("""SELECT * FROM student_tbl""")
display_record = cursor.fetchall()
# Fetch and print records
for x in display_record:
    print(x, '\n')
# Close the cursor and connection
cursor.close()
conn.close()
