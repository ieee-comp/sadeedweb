import os
def rename_files():
    #1. Get file name from folder
    file_list = os.listdir(r"C:\Users\ca07101222\Pictures\pics")
   # print (file_list)
    check_path = os.getcwd()
    print("current dir: " + check_path)
    os.chdir(r"C:\Users\ca07101222\Pictures\pics")
    #2. for each file, rename file
    for file_name in file_list:
        print("Old name: " + file_name)
        table = str.maketrans("", "", "0123456789")
        new_name = file_name.translate(table)
        os.rename(file_name, new_name)
        print("New name: " + new_name)
    os.chdir(check_path)

rename_files()
