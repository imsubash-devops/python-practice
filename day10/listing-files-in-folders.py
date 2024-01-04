import os
folders = input("please provide the list of foldersnames with the spaces in between: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name with correct path, it looks like you enter the wrong folder:" + folder)
        continue  
    except PermissionError:
        print("No access to this folder:" + folder)
        continue     
    print("=== listing files for the folder ---" + folder)

    for file in files:
        print(file)