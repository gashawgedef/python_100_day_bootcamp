

class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer


new_question = Question("What is your name?","False")
print(new_question.text)
