import os, zipfile, glob
from pathlib import Path

folder = Path(input("Enter folder path to backup here: "))

def backuptozip(folder):
    folder = os.path.abspath(folder) # makes sure folder is absolute path

    # Figure out the filename this code should use based on
    # What files already exists
    number = 1
    while True:
        # Example: If folder name is 'Documents', file will be 'Documents_1.zip'
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'

        # Check if a ZIP with that name already exists
        if not os.path.exists(zipfilename):
            break  # Found available name, exit loop
        number = number + 1

    #Create the zip file
    print('Creating %s...' % (zipfilename))
    backupzip = zipfile.ZipFile(zipfilename, 'w')


    files = glob.glob(folder)


    for file in files:
        print('Adding files in %s...' % (file))

        # Add all files (recursively) under the folder
        # '**\\**' is intended to match subdirectories and files inside them
        for filename in glob.glob(os.path.join(folder, "**\\**")):

            # Skip any previous backup ZIPs (avoid recursive zipping)
            newBase = os.path.basename(filename) + '_'
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue # don't backup the backup zip files
            backupzip.write(filename)

        for fil in glob.glob(os.path.join(folder, "**")):
            newBase = os.path.basename(filename) + '_'
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue # don't backup the backup zip files
            backupzip.write(fil)

    backupzip.close() # close the zip file to finalize the backup
    print('Done. Backup created: %s' % zipfilename)
backuptozip(folder)