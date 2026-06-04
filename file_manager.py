# shutil: used to move files from one place to another.
import shutil

# datetime: used to work with dates and times, like creating timestamps for backups.
import datetime

# zipfile: used to create zip files, which are compressed to save space.
import zipfile

# logging: used to log messages, such as errors and information about what the program is doing.
import logging

# pathlib: modern object-oriented library used to manipulate file paths (Replaces os.path and os.walk)
from pathlib import Path

# Basic configuration of the logging system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger("FileManager")

class FileManager:
    def __init__(self, base_directory=None):
        """Initializes the manager with an optional base directory."""
        
        # ITEM 5 FIX: Using Path.cwd() and resolve() to get absolute paths cleanly
        if base_directory:
            self.base_directory = Path(base_directory).resolve()
        else:
            self.base_directory = Path.cwd().resolve()
        
        # ITEM 5 FIX: Using the '/' operator to join paths (much cleaner than os.path.join)
        self.backup_directory = self.base_directory / "_backups"
        self.backup_directory.mkdir(exist_ok=True)
        
        self.categories = {
            "documents": [".pdf", ".doc", ".docx", ".txt"],
            "images": [".jpg", ".jpeg", ".png", ".gif"],
            "audio_video": [".mp3", ".mp4", ".wav", ".avi"],
            "spreadsheets": [".xls", ".xlsx", ".csv"],
            "code": [".py", ".js", ".html", ".css"],
            "others": []  
        }

    def organize_by_extension(self):
        """Organizes files by extension into subfolders."""
        
        for category in self.categories:
            (self.base_directory / category).mkdir(exist_ok=True)
        
        moved_files = 0
        
        # ITEM 5 FIX: iterdir() replaces os.listdir() and returns Path objects
        for item in self.base_directory.iterdir():
            # Only process files, ignore directories
            if item.is_dir():
                continue
            
            # ITEM 5 FIX: .suffix extracts the extension directly, .lower() makes it case-insensitive
            extension = item.suffix.lower()
            target_category = "others"
            
            for category, extensions in self.categories.items():
                if extension in extensions:
                    target_category = category
                    break
            
            try: 
                # ITEM 5 FIX: item.name gets the file name, '/' joins the path
                target = self.base_directory / target_category / item.name
                
                # shutil requires strings or Path objects, Path works perfectly here
                shutil.move(item, target) 
                moved_files += 1 
            except Exception as e: 
                logger.error(f"Error moving {item.name}: {e}")

        logger.info(f"Organization complete: {moved_files} files moved")
        return moved_files

    def create_backup(self, backup_name=None):
        """Creates a compressed backup of the directory."""
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        file_name = f"{backup_name or 'backup'}_{timestamp}.zip"
        backup_path = self.backup_directory / file_name
        
        try:
            with zipfile.ZipFile(backup_path, 'w') as zip_file:
                # ITEM 5 FIX: rglob('*') replaces os.walk(), recursively finding all items
                for file_path in self.base_directory.rglob('*'):
                    # Only add files to the zip, not directories
                    if not file_path.is_file():
                        continue
                    
                    # ITEM 4 FIX: is_relative_to checks if file_path is strictly INSIDE the backup folder
                    # file_path.parts checks if any of the folder names exactly matches "__pycache__"
                    if file_path.is_relative_to(self.backup_directory) or "__pycache__" in file_path.parts:
                        continue
                        
                    # ITEM 5 FIX: relative_to safely gets the relative path for the zip structure
                    rel_path = file_path.relative_to(self.base_directory)
                    zip_file.write(file_path, rel_path)
            
            logger.info(f"Backup created: {backup_path}")
            return str(backup_path) # Return as string just in case external code expects a string
        except Exception as e:
            logger.error(f"Backup error: {e}")
            return None

    def generate_report(self):
        """Generates a simple report of the directory."""
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        report_path = self.base_directory / f"report_{timestamp}.txt"
        
        total_files = 0
        total_directories = 0
        extension_count = {}
        
        # Walks through the entire directory
        for current_path in self.base_directory.rglob('*'):
            
            # ITEM 4 FIX: Safe ignore logic
            if current_path.is_relative_to(self.backup_directory) or "__pycache__" in current_path.parts:
                continue
            
            if current_path.is_dir():
                total_directories += 1
            elif current_path.is_file():
                total_files += 1
                
                # ITEM 5 FIX: Extract extension natively
                ext = current_path.suffix.lower() if current_path.suffix else "(no extension)"
                
                if ext in extension_count:
                    extension_count[ext] += 1
                else:
                    extension_count[ext] = 1
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"DIRECTORY REPORT: {self.base_directory}\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"Total files: {total_files}\n")
            f.write(f"Total folders: {total_directories}\n\n")
            
            f.write("DISTRIBUTION BY EXTENSION:\n")
            for ext, amount in sorted(extension_count.items()):
                f.write(f"{ext}: {amount} file(s)\n")
        
        logger.info(f"Report generated: {report_path}")
        return str(report_path)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="File Manager")
    parser.add_argument("--directory", "-d", help="Directory to process")
    parser.add_argument("command", choices=["organize", "backup", "report"], 
                        help="Command to execute")
    parser.add_argument("--name", "-n", help="Name for the backup")
    
    args = parser.parse_args()
    
    manager = FileManager(args.directory)
    
    if args.command == "organize":
        manager.organize_by_extension()
    elif args.command == "backup":
        manager.create_backup(args.name)
    elif args.command == "report":
        manager.generate_report()