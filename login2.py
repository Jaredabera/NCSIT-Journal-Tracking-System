from tkinter import *
import datetime

def Login():
    """This function creates the Login window and displays it"""

    global user_name_entry
    global password_entry
    global login

    login = Tk()
    login.geometry("500x400")

    login_label = Label(login, text="Login", fg="black")
    login_label.config(font=("Courier", 22))
    user_name_label = Label(login, text="Username:", fg="black")
    password_label = Label(login, text="Password:", fg="black")

    user_name_entry = Entry(login)
    password_entry = Entry(login, show="*")
    submit_button = Button(login, text="Login", fg="blue", command=validate)

    login_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    user_name_label.place(relx=0.4, rely=0.4, anchor=CENTER)
    user_name_entry.place(relx=0.6, rely=0.4, anchor=CENTER)
    password_label.place(relx=0.4, rely=0.5, anchor=CENTER)
    password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)
    submit_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    login.mainloop()

def validate():
    """Validates the user_name and password"""

    user_name = user_name_entry.get()
    password = password_entry.get()

    if user_name == "admin" and password == "root":
        print("Hello Admin")
        login.destroy()
        Admin()
    elif user_name == "publisher" and password == "publisher":
        print("Hello Publisher")
        login.destroy()
        Publisher()
    else:
        label1 = Label(login, text="Invalid Credentials", fg="red")
        label1.place(relx=0.5, rely=0.7, anchor=CENTER)

def Admin():
    admin_panel = Tk()
    admin_panel.geometry("500x400")

    welcome_label = Label(admin_panel, text="Welcome, Admin")
    welcome_label.config(font=("Courier", 18))
    welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    review = Button(admin_panel, text="Review Missing Journals", command=calculate_missing_journals)
    review.place(relx=0.5, rely=0.5, anchor=CENTER)


    admin_panel.mainloop()

def Publisher():
    publisher_panel = Tk()
    publisher_panel.geometry("500x400")

    welcome_label = Label(publisher_panel, text="Welcome, Publisher")
    welcome_label.config(font=("Courier", 18))
    welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    publish_journal = Button(publisher_panel, text="Publish Journal", command=PublishJournal)
    publish_journal.place(relx=0.5, rely=0.5, anchor=CENTER)
    publisher_panel.mainloop()

def PublishJournal():
    global journal_name
    global publish_date
    global published_journals

    published_journals = []
    publish_window = Tk()
    publish_window.geometry("500x400")

    welcome_label = Label(publish_window, text="Enter Journal Details")
    welcome_label.config(font=("Courier", 18))
    welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    journal_name_label = Label(publish_window, text="Journal Name: ")
    publish_date_label = Label(publish_window, text="Publishing date: ")
    journal_name_entry = Entry(publish_window)
    publish_date_entry = Entry(publish_window)
    journal_name_label.place(relx = 0.35, rely=0.3, anchor=CENTER)
    journal_name_entry.place(relx = 0.6, rely=0.3, anchor=CENTER)
    publish_date_label.place(relx= 0.35, rely= 0.4, anchor=CENTER)
    publish_date_entry.place(relx = 0.6, rely=0.4, anchor=CENTER)

    published_journals.append((journal_name, publish_date))

    publish_window.mainloop()


def get_journals():
    # Get the name and publish date from Publisher
    journal_name = journal_name_entry.get()
    publish_date = publish_date_entry.get()
    # Get the arrival date, expiry_date, and booking date from admin
    

    return(journal)

def calculate_missing_journals():
    missing_journals = []

    journal = get_journals()

    """{"Tech Insider":{"pub_type":"Indian",
    "expiry_date": datetime.date(2017,9,29),
    "pub_date":datetime.date(2017,8,1),
    "date_of_booking": datetime.date(2017,9,1),
    "date_of_arrival": datetime.date(2017,9,21)},
    "Dive Deep into Python": {"pub_type":"International",
    "expiry_date": datetime.date(2017,9,29),
    "pub_date":datetime.date(2017,8,1),
    "date_of_booking": datetime.date(2017,9,1),
    "date_of_arrival": datetime.date(2017,9,21)}}
    """

    for jname, jdict in journal.items():
        if jdict["pub_type"] == "Indian":
            # The arrival time is 15 days else it is missing
            if (jdict["date_of_arrival"] - jdict["date_of_booking"]).days >= 15:
                missing_journals.append(jname)
        elif jdict['pub_type'] == "International":
            if (jdict["date_of_arrival"] - jdict["date_of_booking"]).days >= 30:
                missing_journals.append(jname)

    display_missing_journals(missing_journals)

def display_missing_journals(missing_journals):
    """Displays all the missing journals in a new window"""

    missing = Tk()
    missing.geometry("500x400")
    missing_heading = Label(missing, text="The following Journals haven't arrived yet:")
    missing_heading.config(font=("Courier", 12))
    missing_heading.place(relx=0.5, rely=0.1, anchor=CENTER)
    y = 0.2
    count = 1
    for each in missing_journals:
        missing_journal_label = Label(missing, text=str(count) + ". " + each)
        missing_journal_label.place(relx=0.5, rely=y, anchor=CENTER)
        y+=0.1
        count += 1

    missing.mainloop()
# Login()
# Admin()
Publisher()
