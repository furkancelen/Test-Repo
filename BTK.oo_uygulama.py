# Question

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer


# Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions

 
q1 = Question("What is the best programming language?", ["C#", "python", "javascript", "java"], "python")
q2 = Question("What is the most popular programming language?", ["python", "javascript", "C#", "java"], "python")
q3 = Question("What is the highest paying programming language?", ["C#", "javascript",  "java", "python"], "python")
list = [q1, q2, q3]

# print(q1.checkAnswer("python"))