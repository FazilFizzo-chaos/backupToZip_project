# 🗂️ BackupToZip

A simple Python script that **creates a ZIP backup** of a specified folder.  
Each backup is automatically numbered to prevent overwriting previous backups.

---

## 📘 Description

This script allows users to back up any folder by compressing its contents into a `.zip` file.  
Each time the script runs, it checks if a backup already exists and creates a new file such as:
my_folder_1.zip
my_folder_2.zip
my_folder_3.zip


This ensures all backups are safely stored without overwriting previous versions.

---

## ⚙️ Features

- ✅ Backs up an entire folder into a `.zip` file  
- ✅ Automatically names backups to avoid conflicts  
- ✅ Skips previously generated ZIP backup files  
- ✅ Works with all major operating systems (Windows, macOS, Linux)

---

## 🧰 Requirements

This project uses **only built-in Python libraries**, so no installation is needed.

**Built-in modules used:**
- `os`
- `pathlib`
- `zipfile`
- `glob`

---

## 🚀 How to Use

1. **Clone or download** this script:
   ```bash
   git clone https://github.com/your_username/backupToZip_project.git
   cd backupToZip_project
   python backuptoZip.py
   Enter folder path to backup here: D:\Documents
   ```
The script will create a ZIP file (e.g. Documents_1.zip) in the same directory.

### Example
Enter folder path to backup here: D:\Projects\MyApp
Creating MyApp_1.zip...
Adding files in D:\Projects\MyApp...
Done. Backup created: MyApp_1.zip

