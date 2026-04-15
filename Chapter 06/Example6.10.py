from pymongo import MongoClient
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["student"]  # Database name
collection = db["student_tbl"] # Collection name
#  Take input from the user for studentid to delete
student_id = int(input("Enter the student ID to delete: "))
# Delete the record with the matching studentid
delete_result = collection.delete_one({"studentid": student_id})
# Check if a record was deleted
if delete_result.deleted_count > 0:
    print(f"Record with student ID {student_id} deleted successfully.")
else:
    print(f"No record found with student ID {student_id}.")
# Close the connection
client.close()
