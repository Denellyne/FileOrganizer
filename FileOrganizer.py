import os
import time
i = 1

def ChangeFolders(extension,extensionFolder):
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
    i = 0
    userLogin = os.path.expanduser('~')
    parentDirectory = "Downloads"
    
    while (i != 1):
        folderName = "Rar"
        path = os.path.join("C:\\users",userLogin,parentDirectory,folderName)
        if (os.path.isdir(path) != True):
            os.mkdir(path)
        folderName = "Images"
        path = os.path.join("C:\\users",userLogin,parentDirectory,folderName)
        if (os.path.isdir(path) != True):
            os.mkdir(path)
        folderName = "Exe"
        path = os.path.join("C:\\users",userLogin,parentDirectory,folderName)
        if (os.path.isdir(path) != True):
            os.mkdir(path)
        folderName = "Documents"
        path = os.path.join("C:\\users",userLogin,parentDirectory,folderName)
        if (os.path.isdir(path) != True):
            os.mkdir(path)
        i = 1
      
createFolder()

while (i != 0):

    ChangeFolders(extension=".rar",extensionFolder="Rar")
    ChangeFolders(extension=".exe",extensionFolder="Exe")
    ChangeFolders(extension=".zip",extensionFolder="Rar")
    ChangeFolders(extension=".pdf",extensionFolder="Documents")
    ChangeFolders(extension=".docx",extensionFolder="Documents")
    ChangeFolders(extension=".txt",extensionFolder="Documents")
    ChangeFolders(extension=".7z",extensionFolder="Rar")
    ChangeFolders(extension=".zip",extensionFolder="Rar")
    ChangeFolders(extension=".png",extensionFolder="Images")
    ChangeFolders(extension=".jpg",extensionFolder="Images")
    ChangeFolders(extension=".jpeg",extensionFolder="Images")
    time.sleep(1800)
    

    
