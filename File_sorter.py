import os
import shutil

try:
        
    file_location = input("Enter The Folder's Address: ")
    file_types = []

    files = os.listdir(file_location)

    for i in files:
        if os.path.isfile(os.path.join(file_location, i)) and os.path.splitext(i)[1] not in file_types:
            file_types.append(os.path.splitext(i)[1])

    for i in file_types:
        if os.path.isdir(os.path.join(file_location, i[1:])) == False:
            os.mkdir(os.path.join(file_location, i[1:]))

    for i in files:
        f = os.path.join(file_location, i)
        dir_loc = os.path.join(file_location, (os.path.splitext(f)[1])[1:])
        os.rename(f,os.path.join(dir_loc,i))

    shutil.make_archive('C:/Users/Mani/Desktop/Sorted_Files','zip',os.path.dirname(file_location),os.path.basename(file_location))

    print('Done! Zipped Folder Is On Your Desktop!')
    
except FileNotFoundError:
    print("Invalid Address")