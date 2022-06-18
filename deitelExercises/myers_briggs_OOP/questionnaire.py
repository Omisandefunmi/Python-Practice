class Questionnaire:

    def __init__(self):
        self.questions = []
        self.number_of_questions = 0
        self.answers = []
        self.number_of_answers = 0

    def load_questions(self, query):
        self.questions.append(query)
        self.number_of_questions += 1

    def check_number_of_questions(self):
        return len(self.questions)

    def serve_question(self, question_number):
        return self.questions[question_number-1]

    def collect_answers(self, answer):
        if answer == 'a' or answer == 'b':
            self.answers.append(answer)
            self.number_of_answers += 1

    def check_number_of_answers(self):
        return len(self.answers)

