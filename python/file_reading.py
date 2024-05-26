import os
import shutil

parent_dir = os.path.split(os.getcwd())[0]
folder_name = parent_dir + "/files_handling/"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"folder created successfully .....!")
else:
    print(f" folder name :{folder_name} already exists")

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


#deleting file
if os.path.isdir(folder_name):
    shutil.rmtree(folder_name)
    print(f" folder {folder_name} is deleted")
else:
    print(f"no folder is there to delete")
    print(f" folder path: {folder_name}")

print(f"parent_dir :{os.path.split(os.getcwd())})