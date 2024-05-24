import tkinter as tk
from tkinter import ttk
import sv_ttk  # Import the sv_ttk package

class DownloadList:
    def __init__(self, root):
        sv_ttk.use_dark_theme()  # Use the Sun Valley dark theme
        # sv_ttk.use_light_theme()  # Uncomment this line to use the Sun Valley light theme instead

        self.frame = ttk.Frame(root, padding="3 3 12 12")
        self.frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.tree = ttk.Treeview(self.frame, columns=('Status', 'Progress', 'Speed', 'Size'), show='headings')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Progress', text='Progress')
        self.tree.heading('Speed', text='Speed')
        self.tree.heading('Size', text='Size')
        self.tree.pack(expand=True, fill='both')
        self.downloads = {}  # Dictionary to keep track of downloads

    def add_download(self, file_name, status, progress, speed, size):
        # Adds a new download to the tree view
        item_id = self.tree.insert("", "end", values=(status, progress, speed, size))
        self.downloads[file_name] = item_id

    def update_download(self, file_name, status=None, progress=None, speed=None, size=None):
        # Updates an existing download's status in the tree view
        item_id = self.downloads[file_name]
        current_values = list(self.tree.item(item_id, 'values'))
        new_values = [
            status if status is not None else current_values[0],
            progress if progress is not None else current_values[1],
            speed if speed is not None else current_values[2],
            size if size is not None else current_values[3],
        ]
        self.tree.item(item_id, values=new_values)