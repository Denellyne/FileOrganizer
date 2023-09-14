# FileOrganizer
Organizes your files on the download directory
The user needs to change the directory on the python script
Creates folders if they aren't present

Script:

    import os
    import time
    
    i = 0
    
    def ChangeFolders(extension,extensionFolder):
        source = "C:\\Users\\Gustavo Santos\\Downloads"
        files = [x for x in os.listdir(source) if x.endswith(extension)]
    
        destination = "C:\\Users\\Gustavo Santos\\Downloads\\{}".format(extensionFolder)
    
        for file in files:
            src_path = os.path.join(source, file)
            dst_path = os.path.join(destination , file)
            os.rename (src_path , dst_path)
    
    
    def createFolder():
        i = 0
        userLogin = os.environ.get("USERNAME")
        parentDirectory = "Downloads"
        
        while (i != 1):
            for j in range(5):
                match j:
                    case 1:
                        folderName = "Rar"
                        path = os.path.join("C:/users",userLogin,parentDirectory,folderName)
                        if (os.path.isdir(path) != True):
                            os.mkdir(path)
                    case 2:
                        folderName = "Images"
                        path = os.path.join("C:/users",userLogin,parentDirectory,folderName)
                        if (os.path.isdir(path) != True):
                            os.mkdir(path)
                    case 3:
                        folderName = "Exe"
                        path = os.path.join("C:/users",userLogin,parentDirectory,folderName)
                        if (os.path.isdir(path) != True):
                            os.mkdir(path)
                    case 4:
                        folderName = "Documents"
                        path = os.path.join("C:/users",userLogin,parentDirectory,folderName)
                        if (os.path.isdir(path) != True):
                            os.mkdir(path)
        
        
    createFolder()
    
    while (i != 1):
        for j in range(15):
            match j:
                case 1:
                    ChangeFolders(extension=".rar",extensionFolder="Rar")
                case 2:
                    ChangeFolders(extension=".exe",extensionFolder="Exe")
                case 3:
                    ChangeFolders(extension=".zip",extensionFolder="Rar")
                case 4:
                    ChangeFolders(extension=".pdf",extensionFolder="Documents")
                case 5:
                    ChangeFolders(extension=".docx",extensionFolder="Documents")
                case 6:
                    ChangeFolders(extension=".txt",extensionFolder="Documents")
                case 7:
                    ChangeFolders(extension=".7z",extensionFolder="Rar")
                case 8:
                    ChangeFolders(extension=".zip",extensionFolder="Rar")
                case 9:
                    ChangeFolders(extension=".png",extensionFolder="Images")
                case 10:
                    ChangeFolders(extension=".jpg",extensionFolder="Images")
                case 11:
                    ChangeFolders(extension=".jpeg",extensionFolder="Images")
        time.sleep(1800) # 10 Minutes
        
    
        

