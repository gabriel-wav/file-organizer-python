import tkinter as tk
from tkinter import filedialog, messagebox
from file_manager import FileManager  # Imports your translated class from the previous file

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        
        # IMPROVEMENT: Set a default window size so it isn't cramped
        self.root.geometry("350x220")
        
        self.directory = ""

        # Button to choose folder
        tk.Button(root, text="Select Folder", command=self.select_folder).pack(pady=15)

        # Action buttons
        tk.Button(root, text="Organize Files", command=self.organize).pack(fill='x', padx=30, pady=5)
        tk.Button(root, text="Create Backup", command=self.backup).pack(fill='x', padx=30, pady=5)
        tk.Button(root, text="Generate Report", command=self.report).pack(fill='x', padx=30, pady=5)

    def select_folder(self):
        # IMPROVEMENT: Added a title to the selection window to improve UX
        self.directory = filedialog.askdirectory(title="Select a directory to manage")
        if self.directory:
            messagebox.showinfo("Folder Selected", f"Selected directory:\n{self.directory}")

    def check_directory(self):
        """Helper method to verify whether a directory was selected."""
        if not self.directory:
            messagebox.showerror("Error", "No directory selected.")
            return False
        return True

    def organize(self):
        # Use the helper method to avoid repeating code
        if not self.check_directory():
            return
        
        manager = FileManager(self.directory)
        manager.organize_by_extension()
        messagebox.showinfo("Done", "Files organized successfully!")

    def backup(self):
        if not self.check_directory():
            return
            
        manager = FileManager(self.directory)
        path = manager.create_backup()
        
        if path:
            messagebox.showinfo("Backup Created", f"File saved at:\n{path}")
        else:
            messagebox.showerror("Error", "Failed to create backup. Check logs for details.")

    def report(self):
        if not self.check_directory():
            return
            
        manager = FileManager(self.directory)
        path = manager.generate_report()
        messagebox.showinfo("Report Generated", f"File saved at:\n{path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()