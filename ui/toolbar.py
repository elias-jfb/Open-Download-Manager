import tkinter as tk
from tkinter import ttk
import sv_ttk

class Toolbar:
    def __init__(self, root, add_download_callback):
        #sv_ttk.use_light_theme()  # Uncomment this line to use the Sun Valley light theme instead
        sv_ttk.use_dark_theme()
        self.toolbar_frame = ttk.Frame(root, padding="7", width="10")
        self.toolbar_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), columnspan=3)

        # Create a canvas for drawing the add icon
        self.canvas = tk.Canvas(self.toolbar_frame, width=30, height=30, bg="black", bd=0, highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, padx=3)

        # Calculate the coordinates for the plus sign to center it
        center_x, center_y = 30 / 2, 33 / 2
        line_length = 15 / 2
        self.canvas.create_line(center_x - line_length, center_y, center_x + line_length, center_y, fill='gray')
        self.canvas.create_line(center_x, center_y - line_length, center_x, center_y + line_length, fill='gray')

        # Use the canvas as a button by binding a mouse click event to the callback
        self.canvas.bind('<Button-1>', lambda event: add_download_callback())

        root.style = ttk.Style()  # Create a style
        root.style.theme_use('default')  # Use the default theme

if __name__ == "__main__":
    root = tk.Tk()
    toolbar = Toolbar(root, lambda: print("Add Download"))
    root.mainloop()
