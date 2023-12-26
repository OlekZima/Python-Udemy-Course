from typing import List
from question_model import Question


class QuizBrain:
    def __init__(self, questions_list: List[Question]):
        self.questions_list: List[Question] = questions_list
        self.question_number: int = 0
        self.score: int = 0

    def next_question(self):
        current_question: Question = self.questions_list[self.question_number]
        self.question_number += 1
        users_answer: str = self._validate_user_input(
            f"Q.{self.question_number} {current_question.text} (True/False)?: "
        )
        self.check_answer(current_question, users_answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.questions_list)

    def check_answer(self, question: Question, users_answer: str):     

        if users_answer == question.answer.lower():
            print("✅You got it right!")
            self.score += 1
        else:
            print("❌That's wrong.")

        print(f"The correct answer was: {question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")

    @staticmethod
    def _validate_user_input(prompt: str) -> str:
        is_validated = False
        users_answer = ""
        while not is_validated:
            users_answer: str = input(prompt).lower()
            if users_answer not in ["true", "false"]:
                print("Bad input!")
            else:
                is_validated = True

        return users_answer
