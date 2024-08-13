from UI.BaseUI import BaseUI
from UI.LoginUI import LoginUI
from UI.RegisterUI import RegisterUI
import UI.UI_parameters
import tkinter as tk

BLUE = "#87CEEB"
class WelcomeUI(BaseUI):
    def __init__(self, root):
        super().__init__(root)

        # Add title label
        self.title_label = tk.Label(self.root, text="Welcome!", font=("Helvetica", 24), bg=BLUE, fg="white")
        self.title_label.pack(pady=20)

        #Create login and register buttons
        self.login_button = tk.Button(self.root, text="Login", bg=BLUE, fg=BLUE, width=20, height=3,
                                      command=self.login_button_click)
        self.login_button.pack(pady=100)

        self.register_button = tk.Button(self.root, text="Register", bg=BLUE, fg=BLUE, width=20, height=3,
                                         command=self.register_button_click)
        self.register_button.pack(pady=100)

    def login_button_click(self):
        self.clear_widgets()
        LoginUI(self.root)

    def register_button_click(self):
        self.clear_widgets()
        RegisterUI(self.root)
