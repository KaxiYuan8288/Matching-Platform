import tkinter as tk
from UI.WelcomeUI import WelcomeUI
from UI.LoginUI import LoginUI


class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Matching APP")
        WelcomeUI(self.root)

    def run(self):
        self.root.mainloop()


# Create and run the application
if __name__ == "__main__":
    app = Application()
    app.run()
