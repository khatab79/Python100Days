from tkinter import *
from tkinter import messagebox
from os.path import exists
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

    # entry_password.focus()

# ---------------------------- SAVE PASSWORD ------------------------------- #


def check_all_entry():
    web = entry_website.get().strip()
    email_usr = entry_email_username.get().strip()
    password = entry_password.get().strip()

    if len(web) < 3 or len(email_usr) < 3 or len(password) < 3:
        return False

    return True


def add_password():

    lines = []

    if exists('data.txt'):
        with open('data.txt', 'r') as f:
            lines = f.readlines()

    line = f"{entry_website.get()} | {entry_email_username.get()} | {entry_password.get()}\n"

    lines.append(line)

    if check_all_entry():
        is_ok = messagebox.askokcancel(title="Confirm to save", message=f"Your details are :\n"
                                                                        f"Site: {entry_website.get()}\n"
                                                                        f"Email/User Name: {entry_email_username.get()}\n"
                                                                        f"Password: {entry_password.get()}")

        if is_ok:
            with open('data.txt', 'w') as f:
                f.writelines(lines)

            entry_website.delete(0, END)
            entry_password.delete(0, END)
            print("add")

    else:
        messagebox.showwarning(title="Error", message="Empty data or un valid. Please, try again !!!")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=PADDING_IMG, padx=PADDING_IMG)
window.resizable(False, False)
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)

logo_img = PhotoImage(file="logo.png")

lbl_website = Label(text="Website :")
lbl_website.grid(column=0, row=1, pady=PADDING_BETWEEN_LINES)

lbl_email_username = Label(text="Email/Username :")
lbl_email_username.grid(column=0, row=2, pady=PADDING_BETWEEN_LINES)

lbl_email_username = Label(text="Password :")
lbl_email_username.grid(column=0, row=3, pady=PADDING_BETWEEN_LINES)

entry_website = Entry(width=53)
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2)

entry_email_username = Entry(width=53)
entry_email_username.insert(END, "xxxx@xxxx.xx")
entry_email_username.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=31)
entry_password.grid(column=1, row=3)

btn_generate_pw = Button(text="Generate Password", width=16, border=0.5, command=new_password)
btn_generate_pw.grid(column=2, row=3, sticky=W, padx=PADDING_BETWEEN_LINES)

btn_add = Button(text="Add", width=45, command=add_password)
btn_add.grid(column=1, row=4, columnspan=2, pady=PADDING_BETWEEN_LINES)

canvas = Canvas(width=WINDOW_SIZE, height=WINDOW_SIZE)
canvas.create_image(WINDOW_SIZE / 2, WINDOW_SIZE / 2, image=logo_img)

canvas.grid(column=1, row=0)


window.mainloop()
