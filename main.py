import tkinter as tk
from tkinter import ttk
import sv_ttk
from ui.main_window import MainWindow

def main():
    root = tk.Tk()
    app = MainWindow(root)
    sv_ttk.use_dark_theme()  # Use dark theme
    # sv_ttk.use_light_theme()  # Uncomment this line to use light theme instead
    root.mainloop()

if __name__ == '__main__':
    main()