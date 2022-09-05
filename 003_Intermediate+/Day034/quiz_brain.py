import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_nbr = 0
        self.score = 0
        self.question_list = question_list
        self.answer = ""

    def next_question(self):
        current_qts = self.question_list[self.question_nbr]
        self.question_nbr += 1
        unescape_qts = html.unescape(current_qts.text)
        self.answer = current_qts.answer
        return f"Q.{self.question_nbr}: { unescape_qts } "

    def still_has_question(self):
        if self.question_nbr < len(self.question_list):
            return True

    def check_answer(self, user_answer):
        if user_answer.lower() == self.answer.lower():
            self.score += 1
            return True
        else:
            return False

    def results(self):
        return self.score

    # def quzzlier_answer(self):
    #     return self.answer

