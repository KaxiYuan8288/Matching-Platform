from UI.BaseUI import BaseUI
import tkinter as tk

# Define colors
BLUE = "#87CEEB"
class LoginUI(BaseUI):
    def __init__(self, root):
        super().__init__(root)

        # Add title label
        self.title_label = tk.Label(self.root, text="Login", font=("Helvetica", 15), bg=BLUE, fg="white")
        self.title_label.pack(pady=5)

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

        # Add button for login
        self.login_button = tk.Button(self.root, text="Login", bg=BLUE, fg=BLUE,
                                         command=self.login_button_click)
        self.login_button.pack(pady=5)

    def login_button_click(self):
        self.clear_widgets()
        # some function "register"
        # return 0 if the user is logged in - go to home page
        # return 1 if the username does not exist
        # return 2 if the password is incorrect

        '''
        input_user_id = self.user_id_entry.get()
        input_password = self.password_entry.get()

        result = login(input_user_id, input_password)
        if result == 0:
            HomePageUI(self.root, input_user_id)
        elif result == 1:
            message = "User name does not exist, try again!"
            MessageUI(self.root, message)
        elif result == 2:
            message = "Password is incorrect, try again"
            MessageUI(self.root, message)
        '''





