import os
import time

def organizeFiles(extension,extensionFolder):
    userLogin = os.path.expanduser('~')
    parentDirectory = "Downloads"
    source = os.path.join("C:\\users",userLogin,parentDirectory)
    files = [x for x in os.listdir(source) if x.endswith(extension)]

    destination = os.path.join("C:\\users",userLogin,parentDirectory,extensionFolder)

    for file in files:
        src_path = os.path.join(source, file)
        dst_path = os.path.join(destination , file)
        os.rename (src_path , dst_path)

def createFolder():
    userLogin = os.path.expanduser('~')
    parentDirectory = "Downloads"

    folderName = ["Rar","Images","Executables","Documents","Code"]
    for folder in folderName:
        path = os.path.join("C:\\users",userLogin,parentDirectory,folder)
        if (os.path.isdir(path) != True):
            os.mkdir(path)    


if __name__ == "__main__":  
    createFolder()
    extensions = [(".rar","Rar"),(".zip","Rar"),(".7z","Rar"),(".exe","Executables"),(".jar","Code"),(".py","Code"),(".pdf","Documents"),
                  (".docx","Documents"),(".txt","Documents"),(".png","Images"),(".jpg","Images"),(".jpeg","Images")]
    while (True):
        for(extension,folder) in extensions:
            organizeFiles(extension,folder)

        time.sleep(1800)
        

    
