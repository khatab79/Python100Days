import json
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import password_generater

WINDOW_SIZE = 200
PADDING_IMG = 50
PADDING_BETWEEN_LINES = 5


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def new_password():
    if len(entry_password.get()) < 0:
        entry_password.insert(0, password_generater.generate_new_ps())
    else:
        entry_password.delete(0, END)
        entry_password.insert(0, password_generater.generate_new_ps())


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    web = entry_website.get()
    email_usr = entry_email_username.get()
    password = entry_password.get()

    new_data = {
        web: {
            "email": email_usr,
            "password": password,
        }
    }

    if len(web) == 0 or len(email_usr) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Empty data or un valid. Please, try again !!!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        except JSONDecodeError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', 'w') as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)

        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            print("add")


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search():
    web = entry_website.get()

    if len(web) == 0:
        messagebox.showwarning(title="Error", message="Empty data or un valid. Please, try again !!!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                # print(data)

        except FileNotFoundError:
            messagebox.showwarning(title="Error", message=f"Password for { web } not found, search again !!!")

        else:
            if web in data:
                data = data[web]
                password_found = data["password"]
                email_found = data["email"]

                messagebox.showwarning(title=web, message=f"Email: {email_found}\n"
                                                          f"Password: {password_found}")
            else:
                messagebox.showwarning(title="Error", message=f"There is no detail for {web} exist, search again !!!")
        finally:
            print("search")


# ------------------------------- UI SETUP ----------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=PADDING_IMG, padx=PADDING_IMG)
window.resizable(False, False)

logo_img = PhotoImage(file="logo.png")

lbl_website = Label(text="Website :")
lbl_website.grid(column=0, row=1, pady=PADDING_BETWEEN_LINES)

lbl_email_username = Label(text="Email/Username :")
lbl_email_username.grid(column=0, row=2, pady=PADDING_BETWEEN_LINES)

lbl_Password = Label(text="Password :")
lbl_Password.grid(column=0, row=3, pady=PADDING_BETWEEN_LINES)

entry_website = Entry(width=31)
entry_website.focus()
entry_website.grid(column=1, row=1)

entry_email_username = Entry(width=53)
entry_email_username.insert(END, "xxxx@xxxx.xx")
entry_email_username.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=31)
entry_password.grid(column=1, row=3)

btn_search_pw = Button(text="Search", width=16, border=0.5, command=search)
btn_search_pw.grid(column=2, row=1, sticky=W, padx=PADDING_BETWEEN_LINES)

btn_generate_pw = Button(text="Generate Password", width=16, border=0.5, command=new_password)
btn_generate_pw.grid(column=2, row=3, sticky=W, padx=PADDING_BETWEEN_LINES)

btn_add = Button(text="Add", width=45, border=0.5, command=add_password)
btn_add.grid(column=1, row=4, columnspan=2, pady=PADDING_BETWEEN_LINES)

canvas = Canvas(width=WINDOW_SIZE, height=WINDOW_SIZE)
canvas.create_image(WINDOW_SIZE / 2, WINDOW_SIZE / 2, image=logo_img)

canvas.grid(column=1, row=0)

window.mainloop()
