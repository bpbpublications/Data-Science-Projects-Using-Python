from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["student"]#Database name
collection = db["student_tbl"] #Collection (table) name
#Take studentid as input from the user
try:
    student_id = int(input("Enter the student ID to search: "))
except ValueError:
    print("Please enter a valid integer student ID.")
    exit()
#Find the record with given studentid
record = collection.find_one({"studentid": student_id})
# Display the result
if record:
    print("\nStudent Record Found:")
    print("Student ID:", record.get("studentid"))
    print("First Name:", record.get("first_name"))
    print("Last Name:", record.get("last_name"))
    print("Course:", record.get("course"))
else:
    print("\nNo record found with student ID:", student_id)
# Close the connection
client.close()
