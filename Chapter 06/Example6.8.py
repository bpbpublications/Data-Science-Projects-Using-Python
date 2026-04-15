from pymongo import MongoClient
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["student"]   # Database name
collection = db["student_tbl"]  # Collection (table) name
# Update the record where studentid is 1001
collection.update_one(
    {"studentid": 101},   # Filter condition
    {"$set": {"first_name": "Anil", 
              "last_name": "Singh",# Field to update
              "course": "Data Science"}}# Field to update
)
print("Record updated successfully.\n")
# Read and display the updated record
print("Updated Record:")
updated_record = collection.find_one({"studentid": 101})
print(updated_record)
# Close the connection
client.close()
