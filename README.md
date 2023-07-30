# FileOrganizer
Organizes your files on the download directory
The user needs to change the directory on the python script

Script:

    import os
    import time
    
    def ChangeFolders(extension,extensionFolder):
        source = "C:\\Users\\{Username}\\Downloads"
        files = [x for x in os.listdir(source) if x.endswith(extension)]
    
        destination = "C:\\Users\\{UserName}\\Downloads\\{}".format(extensionFolder)
    
        for file in files:
            src_path = os.path.join(source, file)
            dst_path = os.path.join(destination , file)
            os.rename (src_path , dst_path)
    
    i = 0
    
    while (i != 1):
        for j in range(6):
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
        time.sleep(1800) // 10 minutes
