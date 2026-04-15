try:
    f = open("c:\\test1.txt", "r")
    data = f.read()
    print(data)
except FileNotFoundError:
    print("Error: The file does not exist.")
finally:
    print("Closing the file.")
    try:
        f.close()
    except NameError:
        pass
