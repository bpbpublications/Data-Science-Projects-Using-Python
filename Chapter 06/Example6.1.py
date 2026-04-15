import mysql.connector
# Connect to the MySQL server
conn=mysql.connector.connect(
	    host="localhost",   
	    user="root",    
	    password="sasml" 
	)
	# Create a database
db_name = "student"
sql_query = f"CREATE DATABASE IF NOT EXISTS {db_name};"
cursor=conn.cursor()
cursor.execute(sql_query)
# Switch to the new database
conn.database=db_name
# Define a SQL command to create a table
cursor.execute("""CREATE TABLE IF NOT EXISTS student_tbl(studentid INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(255) NOT NULL,last_name VARCHAR(255) NOT NULL,course VARCHAR(255))""")
conn.commit()
conn.close()
print("Database and table created successfully")
