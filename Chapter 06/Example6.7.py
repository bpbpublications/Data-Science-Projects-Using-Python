from pymongo import MongoClient
# Connect to MongoDB
client=MongoClient("mongodb://localhost:27017/")
db = client["student"]  # Database name
collection = db["student_tbl"] # Collection name(like a table)
# Create the record (document)
student_record = {
    "studentid": 101,
    "first_name": "Anil",
    "last_name": "Kumar",
    "course": "Python"
}
# Insert the record into the collection
result = collection.insert_one(student_record)
print("Record inserted successfully. ID:", result.inserted_id)
