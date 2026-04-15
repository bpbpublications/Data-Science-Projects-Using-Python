with open("c:\\test1.txt","w") as file:
     file.write("It is a sample data")
     file.write("Sample data to write into a file")
with open("c:\\test1.txt", "a") as file:
    file.write("Adding a new line at the end.\n")
