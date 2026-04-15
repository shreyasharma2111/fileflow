import os
import shutil
def movefile(source, destination):
    
    #need to create destination folder if it doesn't exist
    os.makedirs(destination, exist_ok=True)
    
    #extract filename from source path
    filename = os.path.basename(source)
    
    #construct the full destination path
    destination_path = os.path.join(destination, filename)
    
    #move the file
    shutil.move(source, destination_path)

    #need to know where file is for logs
    return destination_path
