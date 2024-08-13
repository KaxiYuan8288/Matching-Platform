from UI.BaseUI import BaseUI
from UI.WelcomeUI import WelcomeUI
import tkinter as tk

# Define colors
BLUE = "#87CEEB"

class MessageUI(BaseUI):
    def __init__(self, root, message):
        super().__init__(root)

        # Add title label
        self.title_label = tk.Label(self.root, text="Oops!", font=("Helvetica", 15), bg=BLUE, fg="white")
        self.title_label.pack(pady=5)

        # Add User ID label and entry
        self.user_id_label = tk.Label(self.root, text=message, bg=BLUE, fg="white")
        self.user_id_label.pack(pady=(20, 5))

        # Add button to exit
        self.exit_button = tk.Button(self.root, text="Exit", bg=BLUE, fg=BLUE,
                                      command=self.exit_button_click)
        self.exit_button.pack(pady=5)


    def exit_button_click(self):
        self.clear_widgets()
        WelcomeUI(self.root)
