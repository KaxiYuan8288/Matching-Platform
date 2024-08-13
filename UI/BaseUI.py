import tkinter as tk
import UI.UI_parameters


class BaseUI:

    def __init__(self, root):
        self.root = root
        #Set size, title, background colour.
        self.root.geometry("350x700")
        self.root.title("Matching APP")
        self.root.configure(bg=UI.UI_parameters.BLUE)

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()
