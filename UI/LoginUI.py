from UI.BaseUI import BaseUI
import tkinter as tk

# Define colors
BLUE = "#87CEEB"
class LoginUI(BaseUI):
    def __init__(self, root):
        super().__init__(root)

        # Add title label
        self.title_label = tk.Label(self.root, text="Login", font=("Helvetica", 24), bg=BLUE, fg="white")
        self.title_label.pack(pady=20)

        # Add User ID label and entry
        self.user_id_label = tk.Label(self.root, text="User ID:", bg=BLUE, fg="white")
        self.user_id_label.pack(pady=(20, 5))

        self.user_id_entry = tk.Entry(self.root)
        self.user_id_entry.pack(pady=(0, 20))

        # Add Password label and entry
        self.password_label = tk.Label(self.root, text="Password:", bg=BLUE, fg="white")
        self.password_label.pack(pady=(20, 5))

        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack(pady=(0, 20))





