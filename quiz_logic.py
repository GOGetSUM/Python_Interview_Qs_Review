import random


class QuizLogic:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.used_question = []
        self.question_counter = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def count(self):
        self.question_counter += 1
        return self.question_counter

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.used_question.append(self.question_number)
        next_question_number = 0
        while next_question_number in self.used_question:
            next_question_number = random.randrange(0, len(self.question_list) + 1)
            print(next_question_number)
        q_text = self.question_list[next_question_number]
        print(self.used_question)
        self.question_number = next_question_number
        cont = self.count()
        return f"Q.{self.question_number} in the list, question number {cont}:\n\n {q_text.text}"

    def show_answer(self):
        correct_answer = self.question_list[self.question_number]
        return f"Q.{self.question_number} in the list, question number {self.question_counter}: \n\n{correct_answer.answer}"
