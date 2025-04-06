from question_model import Question
from data import QuestionData
from quiz_brain import QuizBrain
from ui import QuizeInterface


def main():
    data = QuestionData()
    question_data = data.question_data()


    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)


    quiz = QuizBrain(question_bank)
    quize_interface = QuizeInterface(quiz)
    


if __name__ == "__main__":
    main()