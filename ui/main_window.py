import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from downloader.download_manager import DownloadManager
from .menu_bar import MenuBar
from .download_list import DownloadList
from threading import Thread
import os
import re

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Open Download Manager")
        self.menu_bar = MenuBar(root)  # Integrate the menu bar
        self.download_list = DownloadList(root) # integrate the download list
        self.url = tk.StringVar() # Create a StringVar to store the URL
        self.num_chunks = tk.IntVar(value=4) # Create an IntVar to store the number of chunks
        self.save_path = tk.StringVar(value=os.path.expanduser("~/Downloads"))# Create a StringVar to store the save path

        # Setup the UI
        ttk.Label(root, text="URL:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.url, width=50).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(root, text="Number of Parts:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.num_chunks, width=5).grid(row=1, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(root, text="Save to:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.save_path, width=50).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(root, text="Browse", command=self.browse_folder).grid(row=2, column=2, padx=5, pady=5)

        ttk.Button(root, text="Download", command=self.start_download).grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.save_path.set(folder_selected)

    def start_download(self):
        url = self.url.get()
        num_chunks = self.num_chunks.get()
        save_path = self.save_path.get()
        filename = self.get_filename_from_url(url)
        
        if url and save_path:
            downloader = DownloadManager(url, num_chunks, os.path.join(save_path, filename))
            try:
                Thread(target=downloader.download_file).start()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter a URL and select a save location")

def get_filename_from_url(self, url):
    """
    Extracts the filename and keeps its extension from the URL.
    Removes URL parameters to isolate the filename.
    """
    # Attempt to isolate the file name and remove any URL parameters
    filename = re.findall(r'/([^/?]+)[^/]*$', url)
    # Check if a file name is found; if so, return the first match
    if filename:
        return filename[0]
    else:
        # Provide a default filename if none is found
        return 'downloaded_file'

# Create the main window and pass it to the MainWindow class
root = tk.Tk()
app = MainWindow(root)
root.mainloop()
