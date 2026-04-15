from pymongo import MongoClient
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["student"]#Database name
collection = db["student_tbl"]#Collection name
# Take input from user for updating a record
student_id = int(input("Enter Student ID to update: "))
new_first_name = input("Enter new First Name: ")
new_last_name = input("Enter new Last Name: ")
new_course = input("Enter new Course Name: ")
# Update the record
update_result = collection.update_one(
    {"studentid": student_id},
    {
        "$set": {
            "first_name": new_first_name,
            "last_name": new_last_name,
            "course": new_course
        }
    }
)
# Check and display updated record
if update_result.modified_count > 0:
    updated_record = collection.find_one({"studentid": student_id})
    print("\nRecord updated successfully!")
    print("Updated Record:", updated_record)
else:
    print("\nNo record found with that Student ID")
# Close connection
client.close()
