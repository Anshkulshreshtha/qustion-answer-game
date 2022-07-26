from data import question_data
from question_model import Question
from quiz_brain import Quiz_brain

Question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    Question_bank.append(new_question)

quiz = Quiz_brain(Question_bank)

while quiz.should_have_question():
    quiz.next_question()

print("Yey, you have completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(Question_bank)}")
