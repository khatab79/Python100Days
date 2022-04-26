from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

WIDTH_IMG = 200
HEIGHT_IMG = 224

global reps
reps = 0

global stop_timer
stop_timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def act_reset():

    window.after_cancel(stop_timer)
    global reps
    reps = 0

    lbl_check.config(text="")

    lbl_timer.config(text="Timer", fg=GREEN)

    canvas.itemconfig(update_counter, text="00:00")

    # print("reset")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def act_start():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        lbl_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        lbl_timer.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        lbl_timer.config(text="work", fg=GREEN)
    # print("start")

# def act_start():
#     global reps
#     reps += 1
#     if reps == 1 or reps == 3 or reps == 5 or reps == 7:
#         count_down(WORK_MIN * 60)
#     elif reps == 2 or reps == 4 or reps == 6:
#         count_down(SHORT_BREAK_MIN * 60)
#     elif reps == 8:
#         count_down(LONG_BREAK_MIN * 60)
#     print("start")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(update_counter, text=f"{count_min}:{count_sec}")

    if count > 0:
        global stop_timer
        stop_timer = window.after(2, count_down, count-1)
    else:
        act_start()
        check = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check += "\u2713"
        lbl_check.config(text=check)
        if work_sessions == 4:
            act_reset()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

lbl_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW, highlightthickness=0)
lbl_timer.grid(column=1, row=0)


lbl_check = Label(text="", fg=GREEN, font=(FONT_NAME, 15), bg=YELLOW, highlightthickness=0)
lbl_check.grid(column=1, row=3)

btm_start = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=act_start, highlightthickness=0)
btm_start.grid(column=0, row=2)

btm_reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=act_reset, highlightthickness=0)
btm_reset.grid(column=2, row=2)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=WIDTH_IMG, height=HEIGHT_IMG, bg=YELLOW, highlightthickness=0)
canvas.create_image(WIDTH_IMG / 2, HEIGHT_IMG / 2, image=tomato_img)
update_counter = canvas.create_text(WIDTH_IMG / 2, HEIGHT_IMG / 2 + 20, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))

canvas.grid(column=1, row=1)

window.mainloop()
