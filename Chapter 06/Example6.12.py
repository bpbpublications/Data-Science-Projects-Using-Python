from pymongo import MongoClient
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["student"]#Database name
collection = db["student_tbl"] # Table name (Collections)
def insert_record():
    sid = int(input("Enter Student ID: "))
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    course = input("Enter Course: ")
    collection.insert_one({
        "studentid": sid,
        "first_name": fname,
        "last_name": lname,
        "course": course
    })
    print("Record inserted successfully!\n")
def view_all_records():
    print("\nAll Student Records:")
    for record in collection.find():
        print(record)
    print()
def search_by_id():
    sid = int(input("Enter Student ID to Search: "))
    record = collection.find_one({"studentid": sid})
    if record:
        print(record)
    else:
        print("Record not found.\n")
def update_record():
    sid = int(input("Enter Student ID to Update: "))
    fname = input("Enter New First Name: ")
    lname = input("Enter New Last Name: ")
    course = input("Enter New Course: ")
    result = collection.update_one(
        {"studentid": sid},
        {"$set": {
            "first_name": fname,
            "last_name": lname,
            "course": course
        }}
    )
    if result.modified_count:
        print("Record updated.\n")
    else:
        print("No matching record found.\n")
def delete_record():
    sid = int(input("Enter Student ID to Delete: "))
    result = collection.delete_one({"studentid": sid})
    if result.deleted_count:
        print("Record deleted.\n")
    else:
        print("No record found with that ID.\n")
# Menu-driven interface
while True:
    print("1. Add Record\n2. View All Records\n3. Search by ID\n4. Update Record\n5. Delete Record\n6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        insert_record()
    elif choice == '2':
        view_all_records()
    elif choice == '3':
        search_by_id()
    elif choice == '4':
        update_record()
    elif choice == '5':
        delete_record()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid Choice. Try again.\n")
