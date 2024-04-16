##Create an animated font style
#To show credits for copyrights

import sys
import time


message = "Thanks for playing.\n\
All quiz questions are found on these following websites:\n\
\n||Easy questions: https://www.funquizzes.uk/easy-quiz-questions/\n\
\n||Medium questions: https://medium.com/ahaslides-interactive-presentation-software/170-general-knowledge-quiz-questions-and-answers-for-your-next-virtual-pub-quiz-how-big-is-your-f6085c3efc03\n\
\n||Hard Questions: https://ilovenz.me/ultimate-general-knowledge-quiz-new-zealand/https://thoughtcatalog.com/samantha-newman/2020/04/hard-trivia-questions/\n\
"

def animated_txt(message):
    for char in message:
      sys.stdout.write(char) #print it out
      sys.stdout.flush() #to avoid bufetting but flushing imediating

      if char !="\n":
        time.sleep(0.1)
      else:
        time.sleep(1)

animated_txt(message)
