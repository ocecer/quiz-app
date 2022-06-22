import random


class question:
    # Questions in the database
    questionDB = {}
    # Total number of questions in database
    totalQuestionNr = 0

    # Index nr of selected question
    questionIndex = 0

    score = 0
    questionNr = 0

    def __init__(self):
        pass

    def submitQuestion(self, _question, _choices, _answer):
        self.question = _question
        self.choices = _choices
        self.answer = _answer

        if len(question.questionDB.keys()) == 0:
            question.totalQuestionNr = 0
        else:
            question.totalQuestionNr = len(question.questionDB.keys())

        question.questionDB.update({f"Question{question.totalQuestionNr}": [
                                   self.question]+[self.choices]+[self.answer]})

        dummy_questionDB = list(question.questionDB.items())
        random.shuffle(dummy_questionDB)
        question.questionDB = dict(dummy_questionDB)

    def getQuestion(self):
        self.questionDisplay = ""
        self.choicesDisplay = ""
        self.answerDisplay = ""
        self.userAnswer = ""

        if question.questionIndex > question.totalQuestionNr:
            print(f"There are not more questions. Your score is {question.score}.")
        else:
            question.questionNr = list(question.questionDB.keys())[
                question.questionIndex]
            self.questionDisplay = list(question.questionDB.values())[
                question.questionIndex][0]
            self.choicesDisplay = list(question.questionDB.values())[
                question.questionIndex][1]
            self.answerDisplay = list(question.questionDB.values())[
                question.questionIndex][2]

            print(
                f"{question.questionNr}: {self.questionDisplay}\nA: {self.choicesDisplay[0]}\nB: {self.choicesDisplay[1]}\nC: {self.choicesDisplay[2]}\nD: {self.choicesDisplay[3]}")

            self.userAnswer = input("Your answer: ")

            if self.userAnswer == self.answerDisplay:
                question.score += 1
                print(f"Correct answer! Your score is {question.score}.")
            else:
                print(
                    f"Incorrect answer! Answer should have to be {self.answerDisplay}. Your score is {question.score}.")

            question.questionIndex += 1


q1 = question().submitQuestion(
    "aaaa", ["aaaa", "bbbb", "cccc", "dddd"], "aaaa")
q1 = question().submitQuestion(
    "bbbb", ["aaaa", "bbbb", "cccc", "dddd"], "bbbb")
q1 = question().submitQuestion(
    "cccc", ["aaaa", "bbbb", "cccc", "dddd"], "cccc")
q1 = question().submitQuestion(
    "dddd", ["aaaa", "bbbb", "cccc", "dddd"], "dddd")
q1 = question().submitQuestion(
    "eeee", ["eeee", "bbbb", "cccc", "dddd"], "eeee")
print(question.questionDB)
print("\n***********************\n")

gq = question().getQuestion()
gq = question().getQuestion()
gq = question().getQuestion()
gq = question().getQuestion()
gq = question().getQuestion()
gq = question().getQuestion()
# print(gq)
