import os
import shutil


folder_name = os.getcwd() + "/file_reading/"
if os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"folder created successfully .....!")
else:
    print(f" folder name{folder_name} already exists")

#writing a file in given folder

file_name = os.path.join(folder_name,"given_text.txt")

with open(file_name,'w') as file:
    for _ in range(100):
        file.write("Hello World\n")

    file.close()

print(f"file written:{file_name}")

#cross check if file is present

if os.path.isfile(file_name):
    print("file is present")

#reading file

with open(file_name,'r') as file:
    content = file.read()
    print(f" readed files:{content}")


