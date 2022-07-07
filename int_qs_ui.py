from tkinter import *
from quiz_logic import QuizLogic

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_logic: QuizLogic):
        self.quiz = quiz_logic

        self.window = Tk()
        self.window.title("Python Interview Questions to Review")
        self.window.config(padx=10, pady=10, bg=THEME_COLOR)

        self.canvas = Canvas(width=600, height=450, bg="white")
        self.question_text = self.canvas.create_text(
            300,
            200,
            text="Some Question Text",
            fill=THEME_COLOR,
            width=580,
            font=("Arial", 16, "italic"),
        )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        answr_btn_image = PhotoImage(file="images/SHOW_ANSWER.png")
        self.answr_btn = Button(
            image=answr_btn_image, highlightthickness=0, command=self.answer_pressed
        )
        self.answr_btn.grid(row=2, column=0)

        nxt_qs_image = PhotoImage(file="images/NEXT QUESTION.png")
        self.nxt_btn = Button(
            image=nxt_qs_image, highlightthickness=0, command=self.next_question_pressed
        )
        self.nxt_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            count = self.quiz.count

        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the questions to review",
            )
            self.answr_btn.config(state="disable")
            self.nxt_btn.config(state="disable")
            count = self.quiz.count

    def show_answer(self):
        self.canvas.config(bg="white")
        answr_text = self.quiz.show_answer()
        self.canvas.itemconfig(self.question_text, text=answr_text)

    def answer_pressed(self):
        self.window.after(500, self.show_answer)

    def next_question_pressed(self):
        self.window.after(500, self.get_next_question())
