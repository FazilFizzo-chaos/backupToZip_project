import os, zipfile, glob
from pathlib import Path

folder = Path(input("Enter folder path to backup here: "))

def backuptozip(folder):
    folder = os.path.abspath(folder) # makes sure folder is absolute path

    # Figure out the filename this code should use based on
    # What files already exists
    number = 1
    while True:
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
        number = number + 1

    #Create the zip file
    print('Creating %s...' % (zipfilename))
    backupzip = zipfile.ZipFile(zipfilename, 'w')


    files = glob.glob(folder)
    for file in files:
        print('Adding files in %s...' % (file))
        # Add all the files in this folder to the ZIP file
        for filename in glob.glob(os.path.join(folder, "**\\**")):
            newBase = os.path.basename(filename) + '_'
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue # don't backup the backup zip files
            backupzip.write(filename)

        for fil in glob.glob(os.path.join(folder, "**")):
            newBase = os.path.basename(filename) + '_'
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue # don't backup the backup zip files
            backupzip.write(fil)


backuptozip(folder)