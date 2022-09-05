from tkinter import *
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


THEME_COLOR = "#375362"
question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz_brain = QuizBrain(question_bank)


class QuizzlerFace:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.window.config(background=THEME_COLOR)
        self.score = Label(text=f"Score: {0}", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        true_btn_img = PhotoImage(file="images/true.png")

        self.true_btn = Button(image=true_btn_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_btn_click)
        self.true_btn.grid(column=0, row=2)

        false_btn_img = PhotoImage(file="images/false.png")

        self.false_btn = Button(image=false_btn_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_btn_click)
        self.false_btn.grid(column=1, row=2)

        self.reset_btn = Button(text="Reset", command=self.reset)
        self.reset_btn.grid(column=0, row=0)

        self.get_nxt_qts()

        self.window.mainloop()

    def get_nxt_qts(self):
        self.canvas.config(bg="white")
        if quiz_brain.still_has_question():
            self.score.config(text=f"Score: {quiz_brain.score}")
            self.canvas.itemconfig(self.question_text, text=quiz_brain.next_question())
        else:

            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text=f"   End. \nFinal Score is { quiz_brain.score-1}")

    def reset(self):
        global quiz_brain
        for question in question_data:
            question_bank.append(Question(question["question"], question["correct_answer"]))

        quiz_brain = QuizBrain(question_bank)
        quiz_brain.question_nbr = 0
        quiz_brain.score = 0

        self.score.config(text=f"Score: {quiz_brain.score}")
        self.canvas.itemconfig(self.question_text, text="Reset quiz")
        self.true_btn.config(state="active")
        self.false_btn.config(state="active")
        self.window.after(1000, self.get_nxt_qts)

    def true_btn_click(self):
        self.feedback(quiz_brain.check_answer("true"))

    def false_btn_click(self):
        self.feedback(quiz_brain.check_answer("false"))

    def feedback(self, check):
        if check:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_nxt_qts)

