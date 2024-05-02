import tkinter as tk
from tkinter import ttk

class DownloadList:
    def __init__(self, root):
        self.frame = ttk.Frame(root, padding="3 3 12 12")
        self.frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.tree = ttk.Treeview(self.frame, columns=('Status', 'Progress', 'Speed', 'Size'), show='headings')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Progress', text='Progress')
        self.tree.heading('Speed', text='Speed')
        self.tree.heading('Size', text='Size')
        self.tree.pack(expand=True, fill='both')
