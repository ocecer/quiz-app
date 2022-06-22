import random


class question:
    questionDB = {}
    questionNr = 0

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
        self.selectedQuestions_lst = []
        self.selectQuestionNr = 0
        i = 0

        while i <= question.questionNr:
            self.selectQuestionNr = random.randint(0, question.questionNr)
            print(self.selectedQuestions_lst)
            print(self.selectQuestionNr)

            # if any(self.selectQuestionNr == j for j in self.selectedQuestions_lst):
            if self.selectedQuestions_lst.count(self.selectQuestionNr) > 0:
                i += 1
                self.questionFound = False
                continue
            else:
                self.questionFound = True
                break

        if self.questionFound:
            self.selectedQuestions_lst.append(self.selectQuestionNr)
            return question.questionDB.get(f"Question{self.selectQuestionNr}")
        else:
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

gq = question().getQuestion()
print(gq)

gq = question().getQuestion()
print(gq)

gq = question().getQuestion()
print(gq)

gq = question().getQuestion()
print(gq)

gq = question().getQuestion()
print(gq)

gq = question().getQuestion()
print(gq)
