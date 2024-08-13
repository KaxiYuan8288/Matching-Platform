import tkinter as tk

TITLE_FONT_SIZE = 40
FONT = "Arial"
TEXT_FONT_SIZE = 15
GREY =
BLACK =
PINK =
GREEN =
BLUE =

class BaseUI:

    def __init__(self):
        self.root = tk.Tk()
        #Set size, title, background colour.
        self.root.geometry("350x700")
        self.root.title("Matching APP")
        self.root.configure(bg = BLUE)
        self.root.mainloop()