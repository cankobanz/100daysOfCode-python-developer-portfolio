from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Null",
                                                     fill="black",
                                                     font=("Times New Roman", 14, "bold"))

        image_true = PhotoImage(file="../day34-TriviaQuestionAPI/images/true.png")
        self.button_true = Button(image=image_true, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=0)

        image_false = PhotoImage(file="../day34-TriviaQuestionAPI/images/false.png")
        self.button_false = Button(image=image_false, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=2, column=1)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(ms=1000, func=self.get_next_question)



# window = Tk()
# window.title("Pomodoro")
# window.config(padx=100, pady=50, bg=YELLOW)
#
# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(100, 112, image=tomato_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(row=1, column=1)
#
# label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
# label.grid(row=0, column=1)
#
#
# button_start = Button(text="start", command=start_timer)
# button_start.grid(row=2, column=0)
#
# button_reset = Button(text="reset", command=reset_timer)
# button_reset.grid(row=2, column=2)
#
# tick = Label(font=(FONT_NAME, 22, "bold"), bg=YELLOW, fg=GREEN)
# tick.grid(row=2, column=1)