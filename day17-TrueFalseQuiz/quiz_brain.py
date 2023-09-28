class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}. {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.event)

    def still_has_questions(self):
        if len(self.question_list) != self.question_number:
            return True
        else:
            return False

    def check_answer(self, user_answer, real_answer):
        if user_answer == real_answer:
            self.score += 1
            print("You got it right!")
        else:
            print(f"The correct answer was: {real_answer}")

        print(f"Current score is: {self.score}")
