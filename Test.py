import tkinter as tk

TITLE_FONT_SIZE = 18
TITLE_FONT = "Arial"

root = tk.Tk()

root.geometry("350x700")
root.title("Matching APP")

label = tk.Label(root, text = "Login", font = ('Arial', 18))
label.pack(padx=20, padx=20)

textbox = tk.Text(root, height=3, font = ('Arial', 16))
textbox.pack()

button = tk.Button(root, text = "Click Me", font = ('Arial', 18))

root.mainloop()