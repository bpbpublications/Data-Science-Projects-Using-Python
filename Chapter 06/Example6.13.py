from pymongo import MongoClient
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["student"] # Access the 'student' database
collection = db["student_tbl"]# Access the 'student_tbl' collection
# Fetch all records
records = collection.find()
# Display records
print("Student Records from MongoDB:\n")
for record in records:
    print(f"Student ID: {record['studentid']}")
    print(f"First Name: {record['first_name']}")
    print(f"Last Name: {record['last_name']}")
    print(f"Course: {record['course']}")
# Print 30 dashes(-) in a row after each record
    print("-" * 30)
# Close the connection
client.close()
