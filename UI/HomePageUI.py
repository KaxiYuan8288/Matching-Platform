from UI.BaseUI import BaseUI
import tkinter as tk

# Define colors
BLUE = "#87CEEB"
class HomePageUI(BaseUI):
    def __init__(self, root, user_id):
        super().__init__(root)
        #Retrieve recommendations using user_id, return top 5 users
        '''
        result = recommend(user_id)
        for user in result:
            name = user.name
            age = user.age
            address = user.address
            interest = user.interest
        '''