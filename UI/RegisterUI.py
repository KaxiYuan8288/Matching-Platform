from UI.BaseUI import BaseUI
from UI.MessageUI import MessageUI
import tkinter as tk
from tkinter import ttk


BLUE = "#87CEEB"
class RegisterUI(BaseUI):
    def __init__(self, root):
        super().__init__(root)

        self.title_label = tk.Label(self.root, text="Register", font=("Helvetica", 15), bg=BLUE, fg="white")
        self.title_label.pack(pady=5)

        # Create login and register buttons
        self.user_id_label = tk.Label(self.root, text="UserID(Must be unique, 1-8 characters)", bg=BLUE, fg="white")
        self.user_id_label.pack(pady=5)
        self.user_id_entry = tk.Entry(self.root)
        self.user_id_entry.pack(pady=(0, 5))

        self.name_label = tk.Label(self.root, text="Name", bg=BLUE, fg="white")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=(0, 5))

        self.password_label = tk.Label(self.root, text="Password", bg=BLUE, fg="white")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root)
        self.password_entry.pack(pady=(0, 5))

        self.email_label = tk.Label(self.root, text="Email", bg=BLUE, fg="white")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=(0, 5))

        self.gender_label = tk.Label(self.root, text="Gender)", bg=BLUE, fg="white")
        self.gender_label.pack(pady=5)
        self.gender_dropbox = ttk.Combobox(self.root, values = ["Male", "Female"])
        self.gender_dropbox.pack(pady=(0, 5))

        self.age_label = tk.Label(self.root, text="Age", bg=BLUE, fg="white")
        self.age_label.pack(pady=5)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.pack(pady=(0, 5))

        self.address_label = tk.Label(self.root, text="Address(Please enter city name", bg=BLUE, fg="white")
        self.address_label.pack(pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.pack(pady=(0, 5))

        self.interest_label = tk.Label(self.root, text="Interests(Please separate by comma',')", bg=BLUE, fg="white")
        self.interest_label.pack(pady=5)
        self.interest_entry = tk.Text(self.root, height = 3)
        self.interest_entry.pack(pady=(0, 5))

        self.sexual_orientation_label = tk.Label(self.root, text="What gender are you interested in?", bg=BLUE, fg="white")
        self.sexual_orientation_label.pack(pady=5)
        self.sexual_orientation_dropbox = ttk.Combobox(self.root, values=["Male", "Female", "Both genders"])
        self.sexual_orientation_dropbox.pack(pady=(0, 5))

        self.register_button = tk.Button(self.root, text="Register", bg=BLUE, fg=BLUE, command=self.register_button_click)
        self.register_button.pack(pady=5)

    def register_button_click(self):
        self.clear_widgets()
        #some function "register"
        #return 0 if the user is successfully registered
        #return 1 if the username already exists in the database
        #return 2 if the username is not between 1-8 characters
        #return 3 if the email is not valid
        #return 4 if there are empty fields

        '''
        input_user_id = self.user_id_entry.get()
        input_name = self.input.get()
        input_password = self.password_entry.get()
        input_email = self.email_entry.get()
        input_gender = self.gender_dropbox.get()
        input_age = self.age_entry.get()
        input_address = self.address_entry.get()
        input_interest = self.interest_entry.get()
        input_sexual_orientation = self.sexual_orientation_dropbox.get()
        
        result = register(input_user_id, input_name, input_password, input_email, input_gender, input_age,
                            input_address, input_interest, input_sexual_orientation)
        if result == 0:
            message = "Successfully registered, please log in!"
        elif result == 1:
            message = "User name already exists, try again!"
        elif result == 2:
            message = "User name longer than 8 characters, try again!"
        elif result == 3:
            message = "Email is not valid, try again!"
        elif result == 4:
            message = "There are empty fields, try again!"
            
        MessageUI(self.root, message)
        '''

