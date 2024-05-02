import tkinter as tk

class MenuBar:
    def __init__(self, root):
        menubar = tk.Menu(root)
        self.root = root
        self.file_menu = tk.Menu(menubar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=root.quit)

        self.options_menu = tk.Menu(menubar, tearoff=0)
        self.options_menu.add_command(label="Settings", command=self.open_settings)

        menubar.add_cascade(label="File", menu=self.file_menu)
        menubar.add_cascade(label="Options", menu=self.options_menu)

        root.config(menu=menubar)

    def open_settings(self):
        # Logic to open settings window can be added here
        print("Opening settings...")
