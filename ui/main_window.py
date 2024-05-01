import tkinter as tk
from tkinter import ttk
from downloader.download_manager import DownloadManager
from threading import Thread
from tkinter import messagebox

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Download Manager")
        self.url = tk.StringVar()
        self.num_chunks = tk.IntVar(value=4)
        
        # Setup the UI
        ttk.Label(root, text="URL:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.url, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(root, text="Number of Parts:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.num_chunks, width=5).grid(row=1, column=1, padx=5, pady=5, sticky='w')
        ttk.Button(root, text="Download", command=self.start_download).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def start_download(self):
        url = self.url.get()
        num_chunks = self.num_chunks.get()
        if url:
            downloader = DownloadManager(url, num_chunks)
            try:
                Thread(target=downloader.download_file).start()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter a URL")
