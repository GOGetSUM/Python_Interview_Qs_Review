from flash_card_model import Flash_question
from interview_questions import int_quest_answ
from quiz_logic import QuizLogic
from int_qs_ui import QuizInterface


question_bank = []
question_data = list(int_quest_answ.items())

for question in question_data:
    question_text = question[0]
    question_answer = question[1]
    new_question = Flash_question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizLogic(question_bank)
quiz_ui = QuizInterface(quiz)

