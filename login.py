from tkinter import *


class Login:
    """This class contains all the methods required for logging in the system"""

    def __init__(self,master):
        master.title("Login - NCSIT Journal Tracking System")
        master.geometry("500x400")

        self.login_label = Label(root, text="Login", fg="black")
        self.user_name_label = Label(root, text="Username", fg="black")
        self.password_label = Label(root, text="Password", fg="black")

        self.user_name_entry = Entry(root)
        self.password_entry = Entry(root)

        self.submit_button = Button(root, text="Login", fg="blue", command=self.validate)

        self.login_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.user_name_label.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.user_name_entry.place(relx=0.6, rely=0.4, anchor=CENTER)
        self.password_label.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)
        self.submit_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    def validate(self):
        """Validates the user_name and password"""

        self.user_name = self.user_name_entry.get()
        self.password = self.password_entry.get()

        if self.user_name == "admin" and self.password == "root":
            print("Hello Admin")
        elif self.user_name == "publisher" and self.password == "publisher":
            print("Hello Publisher")
        else:
            print("Invalid Credentials")

root = Tk()
login = Login(root)
root.mainloop()
