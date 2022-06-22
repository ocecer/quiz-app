import random


class question:
    # Questions in the database
    questionDB = {}
    # Total number of questions in database
    questionNr = 0

    # list of the idex numbers of selected questions in getQuestion
    selectedQuestions_lst = []
    # Index nr of selected question
    questionIndex = 0

    def __init__(self):
        pass

    def submitQuestion(self, _question, _choices, _answer):
        self.question = _question
        self.choices = _choices
        self.answer = _answer

        if len(question.questionDB.keys()) == 0:
            question.questionNr = 0
        else:
            question.questionNr = int(len(question.questionDB.keys())/3)

        question.questionDB.update({f"Question{question.questionNr}": self.question,
                                   f"Choices{question.questionNr}": self.choices, f"Answer{question.questionNr}": self.answer})

    def getQuestion(self):
        question.questionIndex = random.randint(0, question.questionNr)

        # if any(question.questionIndex == j for j in question.selectedQuestions_lst):
        if question.selectedQuestions_lst.count(question.questionIndex) > 0:
            self.questionFound = False
        else:
            self.questionFound = True
            question.selectedQuestions_lst.append(question.questionIndex)
            return question.questionDB.get(f"Question{question.questionIndex}")

        if not self.questionFound:
            return "There are not any new questions"


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
print(gq)
print(question.selectedQuestions_lst)