class Question:
    def __init__(self, text, options, answer):
        self.question_text = text
        self.question_options = options
        self.true_answer = answer

    def check_answer(self, user_answer):
        return self.true_answer == user_answer


class Quiz:
    def __init__(self, question_list):
        self.questions = question_list
        self.score = 0
        self.question_index = 0

    def get_question(self):
        return self.questions[self.question_index]

    def display_question(self):
        question = quiz.get_question()

        print(f"Question {self.question_index + 1}: {question.question_text}")

        for q in question.question_options:
            print(q)

        user_answer = input("Answer: ").upper()
        self.guess(user_answer)

        self.load_question()

    def guess(self, user_answer):
        question = self.get_question()

        if question.check_answer(user_answer):
            self.score += 25

        self.question_index += 1

    def load_question(self):
        if len(question_list) == self.question_index:
            print("Quiz is done!")

            self.show_score()
        else:
            self.display_progress()
            self.display_question()

    def show_score(self):
        print("Score :", self.score)

    def display_progress(self):
        total_question = len(self.questions)
        question_number = self.question_index + 1

        if question_number > total_question:
            print("Quiz is done!.")
        else:
            print(f" Question {question_number} of {total_question} ".center(100, "-"))


question1 = Question(
    "What is the most popular programming language in 2023?",
    ["A) C#", "B) Java", "C) Python", "D) JavaScript"],
    "C"
)
question2 = Question(
    "Who is the inventor of HTML?",
    ["A) Tim Berners-Lee", "B) Bill Gates", "C) Steve Jobs", "D) Ivan Petrov"],
    "A"
)
question3 = Question(
    "Who is the first computer programmer?",
    ["A) Alan Turing", "B) Ada Lovelace", "C) John von Neumann", "D) Grace Hopper"],
    "B"
)
question4 = Question(
    "In which year was Python developed?",
    ["A) 2000", "B) 1995", "C) 2010", "D) 1989"],
    "D"
)

question_list = [question1, question2, question3, question4]

quiz = Quiz(question_list)
quiz.load_question()
