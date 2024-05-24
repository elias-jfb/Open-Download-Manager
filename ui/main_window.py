import tkinter as tk
from tkinter import filedialog, ttk
from downloader.download_manager import DownloadManager
from .menu_bar import MenuBar
from .download_list import DownloadList
from .toolbar import Toolbar
from threading import Thread
import os

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Open Download Manager")
        self.menu_bar = MenuBar(root)  # Integrate the menu bar
        self.toolbar = Toolbar(root, self.open_add_download_dialog)  # integrate the toolbar
        self.download_list = DownloadList(root) # integrate the download list
        self.url = tk.StringVar() # Create a StringVar to store the URL
        self.num_chunks = tk.IntVar(value=4) # Create an IntVar to store the number of chunks
        self.save_path = tk.StringVar(value=os.path.expanduser("~/Downloads")) # Create a StringVar to store the save path

        # Setup the remaining UI under the toolbar
        self.setup_ui()

    def setup_ui(self):
        # Setup UI components like labels, entries, and buttons below the toolbar
        pass

    def open_add_download_dialog(self):
        # This method will open a dialog to add a new download
        top = tk.Toplevel(self.root)
        top.title("Add New Download")

        # Create a frame to hold the widgets
        frame = ttk.Frame(top, padding="10 10 10 10")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="URL:").grid(row=0, column=0, sticky=tk.W, pady=5)
        url_entry = ttk.Entry(frame, textvariable=self.url, width=50)  # Set width to 50
        url_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(frame, text="Number of Parts:").grid(row=1, column=0, sticky=tk.W, pady=5)
        chunks_entry = ttk.Entry(frame, textvariable=self.num_chunks, width=50)  # Set width to 50
        chunks_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(frame, text="Save Path:").grid(row=2, column=0, sticky=tk.W, pady=5)
        save_path_entry = ttk.Entry(frame, textvariable=self.save_path, width=50)  # Set width to 50
        save_path_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Button(frame, text="Add Download", command=lambda: [self.start_download(), top.destroy()]).grid(row=3, column=0, columnspan=2, pady=10)
        url_entry.focus()

        # Make the entry widgets expand as the window is resized
        frame.columnconfigure(1, weight=1)

    def start_download(self):
        download_path = filedialog.askdirectory(initialdir=self.save_path.get())
        if download_path:
            download_file_name = os.path.join(download_path, os.path.basename(self.url.get()))
            dm = DownloadManager(self.url.get(), self.num_chunks.get(), self.download_list, download_file_name)
            thread = Thread(target=dm.download_file)
            thread.start()
