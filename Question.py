#This is the blueprint that will hold the Output of the Questions and the Input of the user
class Question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer
