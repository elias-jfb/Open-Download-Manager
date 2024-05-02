import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from downloader.download_manager import DownloadManager
from .menu_bar import MenuBar
from .download_list import DownloadList
from .toolbar import Toolbar
from threading import Thread
import os
import re

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Open Download Manager")
        self.menu_bar = MenuBar(root)  # Integrate the menu bar
        self.toolbar = Toolbar(root, self.open_add_download_dialog)  # integrate the toolbar
        self.download_list = DownloadList(root) # integrate the download list
        self.url = tk.StringVar() # Create a StringVar to store the URL
        self.num_chunks = tk.IntVar(value=4) # Create an IntVar to store the number of chunks
        self.save_path = tk.StringVar(value=os.path.expanduser("~/Downloads"))# Create a StringVar to store the save path

        # Setup the remaining UI under the toolbar
        self.setup_ui()

    def setup_ui(self):
        # Setup UI components like labels, entries, and buttons below the toolbar
        pass

    def open_add_download_dialog(self):
        # This method will open a dialog to add a new download
        top = tk.Toplevel(self.root)
        top.title("Add New Download")
        ttk.Label(top, text="URL:").grid(row=0, column=0)
        url_entry = ttk.Entry(top, textvariable=self.url)
        url_entry.grid(row=0, column=1)
        
        ttk.Label(top, text="Number of Parts:").grid(row=1, column=0)
        chunks_entry = ttk.Entry(top, textvariable=self.num_chunks)
        chunks_entry.grid(row=1, column=1)

        ttk.Button(top, text="Add Download", command=lambda: [self.start_download(), top.destroy()]).grid(row=2, column=0, columnspan=2)
        url_entry.focus()

    def start_download(self):
        # Download starting logic, which now can be invoked from the toolbar button as well
        download_path = filedialog.askdirectory(initialdir=self.save_path.get())
        if download_path:
            dm = DownloadManager(self.url.get(), self.num_chunks.get(), self.download_list)
            thread = Thread(target=dm.download_file)
            thread.start()
