# Import required libraries
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import requests
from threading import Thread
import os

# Define the Downloader class
class Downloader:
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

    def download_chunk(self, url, start, end, filename):
        headers = {'Range': f'bytes={start}-{end}'}
        response = requests.get(url, headers=headers, stream=True)
        with open(filename, "r+b") as f:
            f.seek(start)
            f.write(response.content)

    def download_file(self):
        url = self.url.get()
        num_chunks = self.num_chunks.get()
        response = requests.head(url)
        filesize = int(response.headers['Content-Length'])
        chunk_size = filesize // num_chunks
        threads = []
        
        with open('downloaded_file', 'wb') as f:
            f.truncate(filesize)
        
        for i in range(num_chunks):
            start = i * chunk_size
            end = start + chunk_size - 1
            if i == num_chunks - 1:
                end = filesize - 1
            thread = Thread(target=self.download_chunk, args=(url, start, end, 'downloaded_file'))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        messagebox.showinfo("Download Complete", "Your file has been downloaded successfully!")

    def start_download(self):
        if self.url.get():
            try:
                Thread(target=self.download_file).start()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter a URL")

# Create the main window and pass it to the Downloader class
root = tk.Tk()
app = Downloader(root)
root.mainloop()
