import tkinter as tk
from tkinter import ttk

class Toolbar:
    def __init__(self, root, add_download_callback):
        self.toolbar_frame = ttk.Frame(root, padding="2 2 2 2")
        self.toolbar_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), columnspan=3)

        # Create a canvas for drawing the add icon
        self.canvas = tk.Canvas(self.toolbar_frame, width=20, height=20)
        self.canvas.pack(side=tk.LEFT, padx=2)

        # Draw a simple plus sign
        self.canvas.create_line(10, 4, 10, 16, fill='black')
        self.canvas.create_line(4, 10, 16, 10, fill='black')

        # Use the canvas as a button by binding a mouse click event to the callback
        self.canvas.bind('<Button-1>', lambda event: add_download_callback())
