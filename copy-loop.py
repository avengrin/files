# importing the module
import os
import shutil

# Fetching all the files to directory
parent_dir = "E:/movies/"
source_dir = "C:/Users/trion/video"

for i in range(2):
    directory = f"movie{i}" 
    path = os.path.join(parent_dir, directory)
    # os.mkdir(path)
    shutil.copytree(source_dir, path)
    print("Directory '% s' copied" % directory) 
    # shutil.copytree('C:\Users\trion\','C:\Users\Lenovo\Downloads\Work TP\/newfolder')
    # print("File Copied Successfully")