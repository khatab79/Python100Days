from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
MY_SCREEN = 50
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
WAITING_TIME = 3000

current_word = {}
to_learn = {}

try:
    data = pandas.read_csv("data/learn_french_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
except pandas.errors.EmptyDataError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_word, flip_time
    window.after_cancel(flip_time)
    if len(to_learn) > 0:
        current_word = random.choice(to_learn)
        canvas.itemconfig(canvas_title, text="French", fill="black")
        canvas.itemconfig(canvas_word, text=current_word["French"], fill="black")
        canvas.itemconfig(canvas_img, image=card_front_img)
        flip_time = window.after(WAITING_TIME, flip_card)


def flip_card():
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_word["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back_img)


def known_card():
    global to_learn
    if len(to_learn) > 0:
        to_learn.remove(current_word)
        print(len(to_learn))
        data = pandas.DataFrame(to_learn)
        data.to_csv("data/learn_french_words.csv", index=False)
        next_card()
    else:
        canvas.itemconfig(canvas_title, text="Good Job", fill="black")
        canvas.itemconfig(canvas_word, text="No more word.\n Start again", fill="black", font=("Ariel", 30, "bold"))
        canvas.itemconfig(canvas_img, image=card_front_img)
        reload_list = pandas.read_csv("data/french_words.csv")
        to_learn = reload_list.to_dict(orient="records")


window = Tk()
window.title("Flashy")
window.config(padx=MY_SCREEN, pady=MY_SCREEN, bg=BACKGROUND_COLOR)

flip_time = window.after(WAITING_TIME, flip_card)

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas_img = canvas.create_image(int(CANVAS_WIDTH/2), int(CANVAS_HEIGHT/2), image=card_front_img)
canvas_title = canvas.create_text(int(CANVAS_WIDTH/2), int(CANVAS_HEIGHT/2-120), text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(int(CANVAS_WIDTH/2), int(CANVAS_HEIGHT/2), text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=known_card)
right_btn.grid(row=1, column=1)

next_card()

window.mainloop()