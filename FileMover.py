import os, shutil

source = input("Enter the source directory for your files:\n\t")

dest = input("Enter the destination directory for your files:\n\t")


for folderName, subFolders, fileNames in os.walk(source):
    for fileName in fileNames:
        
        print(f"Moving {fileName} to {dest}....")

        filePath = os.path.join(folderName, fileName)
        newPath = os.path.join(dest, fileName)

        shutil.move(filePath, newPath)

        print(f'Moved {fileName} to {newPath}')