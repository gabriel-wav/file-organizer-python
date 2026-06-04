# 🗄️ Python File Organizer

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

A command-line and graphical interface utility to organize files by extension, create compressed backups, and generate directory reports.

---

## 📖 Fictional Scenario

> A database company called DWC suffered a hacker attack that breached their systems, scrambling all stored content. After searching for a solution, DWC found our team and requested help to fix the problem. We accepted the challenge and built this tool to restore order.

---

## ✨ Key Features

* **Automatic Organization**: Moves files into folders named according to their extensions (e.g., `documents`, `images`, `videos`).
* **Backup Creation**: Generates a `.zip` file containing all files from the specified directory, with a timestamp for version control.
* **Report Generation**: Creates a text file (`.txt`) with a summary of the directory contents, including a file count per extension.
* **Dual Interface**: Can be used either through a simple graphical user interface (GUI) built with Tkinter, or via the command line (CLI) for automation and scripting.

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** for the graphical interface (Python standard library).
* **Native Libraries:** `os`, `shutil`, `datetime`, `zipfile`, `logging`, `argparse`, `pathlib`.

---

## 🚀 How to Use

No external packages need to be installed. Just clone this repository:

```bash
git clone [https://github.com/gabriel-wav/separador-de-arquivos.git](https://github.com/gabriel-wav/separador-de-arquivos.git)
cd separador-de-arquivos
```

You can use the tool in two ways:

### 1. Using the Graphical Interface (GUI)

This is the easiest and most visual way to use the program. Run the following command in your terminal:

```bash
python interface.py
```

A window will open with the following options:

- **Select Folder**: Click to choose the directory you want to manage.
- **Organize Files**: After selecting a folder, click to move files into subfolders by type.
- **Create Backup**: Creates a `.zip` backup of the selected folder.
- **Generate Report**: Creates a `.txt` file with the folder's statistics.

### 2. Using the Command Line (CLI)

For advanced users or scripting purposes, you can use `file_manager.py` directly from the terminal.

**Command structure:**
```bash
python file_manager.py [command] --directory "/path/to/your/folder"
```

**Available commands:**

#### `organize`: Organizes the files in the specified directory.

```bash
python file_manager.py organize --directory "C:\Users\YourUser\Downloads"
```

#### `backup`: Creates a backup of the directory. You can specify a custom name for the backup file.

```bash
# Backup with default name (e.g.: backup_2025-06-08_093000.zip)
python file_manager.py backup --directory "C:\Users\YourUser\Documents"

# Backup with custom name
python file_manager.py backup --directory "C:\Users\YourUser\Documents" --name "Final_Project_Backup"
```

#### `report`: Generates a content report for the directory.

```bash
python file_manager.py report --directory "C:\Users\YourUser\Images"
```

---

## 👨‍💻 Authors & Contributions

This project was developed as a team, with the following contributions:

**Antonio Ferreira** ([@Antoniojferreira3](https://github.com/Antoniojferreira3)):
- Development of the main class initialization (`__init__`).
- Creation of the graphical interface with Tkinter (`interface.py`).

**Danilo Gutierre** ([@danilinhotj187](https://github.com/danilinhotj187)):
- Implementation of the file organization function by extension (`organize_by_extension`).

**Gabriel Fernandes** ([@gabriel-wav](https://github.com/gabriel-wav)):
- Implementation of the backup creation function in `.zip` format (`create_backup`).
- **Recent Updates:** Independently refactored the entire codebase to use modern libraries (`pathlib`), fixed critical counter bugs, improved folder exclusion logic, and translated the project to English.

**Pedro Henrique** ([@pedroH901](https://github.com/pedroH901)):
- Implementation of the report generation function (`generate_report`).
- Configuration of the command-line interface using `argparse`.
