import os
import shutil
import time

time.gmtime()
time.asctime()

path = input("enter the name of the directory to sorted :-")

list_of_files = os.listdir(path)

for files in list_of_files:
    name, ext = os.path.splitext(files)

    ext = ext[1:]

    if ext == '':
        continue

if os.path.exists(path+'/'+ext):
    shutil.move(path+'/'+files,path+'/'+ext+'/'+files)

else:
    os.makedirs(path+'/'+ext)
    shutil.move(path+'/'+files, path+'/'+ext+'/'+files)

ctime = os.stat(path).st_ctime

return ctime