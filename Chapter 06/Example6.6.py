# Import MongoClient
from pymongo import MongoClient
# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB")
# Create or connect to a database named 'student'
db = client["student"]
print("Database 'student' created or connected")
# Create or connect to a collection (table) named 'student_tbl'
collection = db["student_tbl"]
print("Collection 'student_tbl' created or connected")
