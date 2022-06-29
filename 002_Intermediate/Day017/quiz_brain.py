class QuizBrain:
    
    def __init__(self, question_list):
        self.question_nbr = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_qts = self.question_list[self.question_nbr]
        self.question_nbr += 1
        # qts = "Q" + self.question_nbr + ":" + self.question_list[self.question_nbr - 1].text + " (True/False)?: "
        qts = f"Q.{ self.question_nbr }: { current_qts.text } (True/False)?: "

        answer = input(qts)
        self.check_answer(answer,current_qts.answer)


    def still_has_question(self):
        return self.question_nbr < len(self.question_list) 

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: { correct_answer }")
        print(f"Your current score is: { self.score }/{ self.question_nbr }")

    def final_results(self):
        print("You have completed the quiz")
        print(f"Your final score was: { self.score }/{ self.question_nbr }")
    

    