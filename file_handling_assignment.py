def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("My name is Barrack Amuyunzu\n")
            file.write("Am Luhya\n")
            file.write("I am from Kenya Nairobi county\n")
    except IOError as e:
        print("Error creating file:", e)
    finally:
        print("File creation process completed.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError as e:
        print("Error reading file:", e)

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
             file.write("My name is  Amuyunzu\n")
             file.write("Am Kikuyu\n")
             file.write("I am from Kenya Nairobi county\n")
    except PermissionError as e:
        print("Error appending to file:", e)

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Displaying content after appending
