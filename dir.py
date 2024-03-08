# Write a Python program to list only directories, files and all directories, files in a specified path.
import os 
import string
path = r"/Users/b3knur/Desktop/LAB 6"
all = list(os.listdir(path))
print(all)

# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
def check_access(path):
    if not os.path.exists(path):
        print("path doesn't exist")
        return 
    else:
        print('path does exist')
        if os.access(path, os.R_OK):
            print("readable")
        else:
            print("don't readable")
        if os.access(path, os.W_OK):
            print("writable")
        else:
            print("don't writable")
        if os.access(path, os.X_OK):
            print("executable")
        else:
            print("don't executable")

if __name__ == "__main__":
    path_to_check = r"/Users/b3knur/Desktop/LAB 6"

check_access(path_to_check)

# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
def checker(path):
    if os.path.exists(path):
        print("Name of file: ", os.path.basename(path))
        print("name of directory: ", os.path.dirname(path))
        return "success"
    
print(checker(path))

# Write a Python program to count the number of lines in a text file.
with open("sometext.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()

# Write a Python program to write a list to a file.
def writesome(list_of_elements):
    with open("sometext.txt", '+a') as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
        f.close()
    return 0

writesome([12345, 56789, 90987654, "dfghjkl"])

# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("hello world")

if __name__ == "__main__":
    generate_files() 

# Write a Python program to copy the contents of a file to another file
def copier():
    string = str(input("Enter the name of file: "))
    with open(string) as file:
        data = file.read()
    file.close()
    copy_path = ""
    for i in range(len(string)):
        if string[i]=='.':
            copy_path+='_1'
        copy_path+=string[i]
    with open(copy_path, "+w") as file_copy:
        file_copy.write(data)
    file.close()
    
    return 0

copier()

# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            try:
                os.remove(path)
                print(f"Файл '{path}' успешно удален.")
            except Exception as e:
                print(f"Ошибка при удалении файла: {e}")
            else:
                print("The file deleted")
        else:
            print(f"Отсутствует право на запись в файл '{path}'.")
    else:
        print(f"Файл '{path}' не существует.")

delete_file(r"/Users/b3knur/Desktop/LAB 6")