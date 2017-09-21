from tkinter import *


class Login:
    """This class contains all the methods required for logging in the system"""

    def __init__(self,master):
        # master.geometry("500x400")
        loginframe = Frame(master)

        self.login_label = Label(loginframe, text="Login", fg="black")
        self.login_label.config(font=("Courier", 22))
        self.user_name_label = Label(loginframe, text="Username:", fg="black")
        self.password_label = Label(loginframe, text="Password:", fg="black")

        self.user_name_entry = Entry(loginframe)
        self.password_entry = Entry(loginframe, show="*")
        self.submit_button = Button(loginframe, text="Login", fg="blue", command=self.validate(master))

        self.login_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.user_name_label.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.user_name_entry.place(relx=0.6, rely=0.4, anchor=CENTER)
        self.password_label.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)
        self.submit_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    def validate(self, master):
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
root.title("NCSIT Journal Tracking System")
root.geometry("500x400")
login = Login(root)
root.mainloop()
