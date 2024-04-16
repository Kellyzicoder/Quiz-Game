#A modified version of my 1st and 2nd game versions

#assembled all codes together

import time
import threading
import sys

#This is the blueprint that will hold the Output of the Questions and the Input of the user
from Question import Question
#will use this for my spaces in which the time and the points go in one place
global x
x = " " * 20

global Q
Q = 0  #number of questions

####################### FUNCTIONS ###########################

#LEVEL1QUESTIONS
question_prompts = [
    "What colour are the four stars on the flag of New Zealand?\n(a) Yellow\n(b) Red\n(c) White\n(d) Green\nAnswer: ",
    "What are made and repaired by a cobbler?\n(a) Sink\n(b) Toilet Seat\n(c) Shoes\n(d) Utensils\nAnswer: ",
    "Which is the country with the biggest population in Europe?\n(a) Russia\n(b) China\n(c) Australia\n(d) Nigeria\nAnswer: ",
    "Which English king married six times?\n(a) Harold Godwinson\n(b) Anne Boleyn\n(c) Henry VII of England\n(d) None of the above\nAnswer: ",
    "H2O is the chemical formula for what?\n(a) Salt\n(b) Gastrocemius\n(c) Hydrogen \n(d) Water\nAnswer: "
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "d"),
]


def run_test(questions):
    valid = False

    score = 0

    global play_points
    play_points = score + 100

    for question in questions:
        print()
        print()
        answer = input(question.prompt).lower()

        #This code is for no input by user which is a loop for user to input something before they can continue
        if answer == "":
            print("Please type something.")
            print()
            while not valid:
                answer = input(question.prompt).lower()

                if answer == "":
                    print("Please type something.")
                    print()
                    valid = False
                elif answer == question.answer:
                    score += 1
                    print("Correct. Well done. You got a point")
                    break
                else:
                    print("Wrong answer")
                    break

        elif answer == question.answer:
            score += 1
            print("Correct. Well done. You got a point")
        else:
            print("Wrong answer")

    print()
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    time.sleep(1)

    if score == 0:
        print("You have another chance. Try to get them right this time!")
        time.sleep(0.5)
        run_test(questions)
    else:
        print()
        print()
        print(
            "You have been awarded a bonus of 100 points to start Level 2 quiz"
        )
        play_points = score + 100
        print("Your points is " + str(play_points))
    return


#mode displaying functions
def mode_run():
    time.sleep(3.5)
    print("\n\n\n\nLevel 2:\nChoose one of these to start: ")
    print()
    print(
        " 1)Easy mode (level_1points)  \n minus 30 points for wrong answer \n Timer: 1 min(s) and 30 sec(s)"
    )
    time.sleep(0.8)
    print(
        "\n 2)Medium mode (level_1points)* 200 points  \n minus 80 points for wrong answer \n Timer: 60sec(s)"
    )
    time.sleep(0.8)
    print(
        "\n 3)Hard mode ((level_1points)* 500 points) \n minus 180 points for wrong answer \n Timer: 30sec(s)"
    )
    time.sleep(0.9)
    print()
    print()
    return


#a function to call when there is no more point left and display results
def no_points_end(var_score):

    #easyquestions part
    if question == questions2[10] and med_play_points <= 0:
        time.sleep(0.8)
        print(
            "\n\n*** Oops! You were so CLOSE and had yourself some NEGATIVE points. *** \n\nBut well done because you have answered all questions. Your current points was '{}' and the amount of time left was '{}'. "
            .format(play_points, my_timer))
        return

    #mediumquestions part
    elif question == questions3[10] and med_play_points <= 0:
        time.sleep(0.8)
        print(
            "\n\n*** Oops! You were so CLOSE and had yourself some NEGATIVE points. *** \n\nBut well done because you have answered all questions. Your current points was '{}' and the amount of time left was '{}'. "
            .format(med_play_points, my_timer))
        return

    #hardquestions part
    elif question == questions4[10] and hard_play_points <= 0:
        time.sleep(0.8)
        print(
            "\n\n*** Oops! You were so CLOSE and had yourself some NEGATIVE points. *** \n\nBut well done because you have answered all questions. Your current points was '{}' and the amount of time left was '{}'. "
            .format(hard_play_points, my_timer))
        return

    #for users that don't get to answer all the questions and their points is <=0
    else:
        print("\n\n***Sorry you run out of points. Game Over***")
        print("You answered " + str(Q) +
              " questions in total. Your current score was " + str(var_score))
    return


#a function to call when time is up and display results
def no_time_end(var_score):

    #easyquestions part
    if question == questions2[
            10] and my_timer == '  00 min(s), 00 sec(s)' and play_points <= 0:
        time.sleep(0.8)
        print(
            "\n\n*** Oops! You run out of TIME and you got yourself some NEGATIVE points. *** \n\nBut well done because you have answered all questions. Your current points was '{}' and the amount of time left was '{}' "
            .format(play_points, my_timer))
        return
    elif question == questions2[10] or questions3[10] or questions4[
            10] and my_timer == '  00 min(s), 00 sec(s)' and play_points > 0:
        time.sleep(0.8)
        print(
            "\n\n*** Oops! You run out of TIME ***.\n\nBut well done because you have answered all questions. Your current points was '{}' and the amount of time left was '{}' "
            .format(play_points, my_timer))
        return

    #mediumquestions part
    elif question == questions3[
            10] and my_timer == '  00 min(s), 00 sec(s)' and med_play_points <= 0:
        time.sleep(0.8)
        print(
            "\n\n*** Oops! You run out of TIME and you got yourself some NEGATIVE points. *** \n\nBut well done because you have answered all questions. Your current points was '{}' and the amount of time left was '{}' "
            .format(med_play_points, my_timer))
        return
    elif question == questions3[
            10] and my_timer == '  00 min(s), 00 sec(s)' and med_play_points > 0:
        time.sleep(0.8)
        print(
            "\n\n*** Oops! You run out of TIME ***.\n\nBut well done because you have answered all questions. Your current points was '{}' and the amount of time left was '{}' "
            .format(med_play_points, my_timer))
        return

    #hardquestions part
    elif question == questions4[
            10] and my_timer == '  00 min(s), 00 sec(s)' and hard_play_points <= 0:
        time.sleep(0.8)
        print(
            "\n\n*** Oops! You run out of TIME and you got yourself some NEGATIVE points. *** \n\nBut well done because you have answered all questions. Your current points was '{}' and the amount of time left was '{}' "
            .format(hard_play_points, my_timer))
        return
    elif question == questions4[
            10] and my_timer == '  00 min(s), 00 sec(s)' and hard_play_points > 0:
        time.sleep(0.8)
        print(
            "\n\n*** Oops! You run out of TIME ***.\n\nBut well done because you have answered all questions. Your current points was '{}' and the amount of time left was '{}' "
            .format(hard_play_points, my_timer))
        return

    #for users that don't get to answer all the questions on time
    else:
        print("\n\n***You run out of TIME***")
        print("You answered " + str(Q) +
              " questions in total. Your current score was " +
              str(var_score))
    return


#countdown for the timer
def countdown(t):
    global my_timer

    if t == 30:
        for _ in range(t):
            t -= 1
            mins, secs = divmod(t, 60)
            my_timer = '  {:02} sec(s)'.format(mins, secs)
            time.sleep(1)
        return

    elif t == 90 or 60:
        for _ in range(t):
            t -= 1
            mins, secs = divmod(t, 60)
            my_timer = '  {:02d} min(s), {:02} sec(s)'.format(secs)
            time.sleep(1)
        return
    else:
      pass
      


#For output staments to keepthem arranged and orderly
def output_statement(statement, char):
    print()
    print(char * 31 + str(" " * 13) + char * 40)
    print(statement)
    print(char * 31 + str(" " * 13) + char * 40)
    #print(char*len(statement))
    print


#counting down before the start of Level 1
def intro_counter(t):
    secs = [5, 4, 3, 2, 1, 0]
    for sec in secs:
        print("~~ Game starts in {}... ~~".format(sec), end="\r")
        time.sleep(t)
    print("\nGoodluck!")


##Create an animated font style
#To show credits for copyrights
message = "Thanks for playing.\n\
All quiz questions are found on these following websites:\n"

message2 = "\n||Easy questions: https://www.funquizzes.uk/easy-quiz-questions/\n"

message3 = "\n||Medium questions: https://medium.com/ahaslides-interactive-presentation-software/170-general-\nknowledge-quiz-questions-and-answers-for-your-next-virtual-pub-quiz-how-big-is-your\n-f6085c3efc03\n"
message4 = "\n||Hard Questions: https://ilovenz.me/ultimate-general-knowledge-quiz-new-zealand/https://thoughtcatalog.com/samantha-newman/2020/04/hard-trivia-questions/\n\n\n"


def animated_txt(message):
    for char in message:
        sys.stdout.write(char)  #print it out
        sys.stdout.flush()  #to avoid bufetting but flushing imediating

        if char != "\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

    for x in range(0, 1):
        if char != "\n":
            pass
        else:
            print(message2)
            time.sleep(1.5)
            print(message3)
            time.sleep(1.5)
            print(message4)
            time.sleep(1.5)


### EASY QUESTIONS ###
question_2prompts = [
    "In which country was Adolf Hitler born? \n(a) Belgium\n(b) Germany\n(c) Austria\n(d) Poland)\nAnswer: ",
    "The phrase ‘three strikes and you’re out’ originates from which sport?\n(a) Baseball\n(b) Volleyball\n(c) Table Tennis\n(d) Cricket\nAnswer: ",
    "Which is the country with the biggest population in Europe?\n(a) Russia\n(b) China\n(c) Australia\n(d) Nigeria\nAnswer: ",
    "Which English king married six times?\n(a) Harold Godwinson\n(b) Anne Boleyn\n(c) Henry VII of England\n(d) None of the above\nAnswer: ",
    "Is water considered colourless rather than white?\n(a) True  \n(b)False\nAnswer: ",
    "How many states make up the United States of America?\n(a) 60\n(b) 50\n(c) 70\n(d) 80\nAnswer: ",
    "In the medical profession, what do the initials ‘GP’ stand for?\n(a) General Professor\n(b) doctor\n(c) General Practitioner\nAnswer: ",
    "Which pair of superheroes are known as the ‘Dynamic Duo’?\n(a) Wolferine and NightCrawler\n(b) Batman and Robin\nAnswer: ",
    "In which sport may a player score a birdie, eagle or albatross?\n(a) Table Tennis\n(b) Volleyball\n(c) American Football\n(d) Golf\nAnswer: ",
    "The underwater city of Bikini Bottom is the setting for which popular children’s cartoon?\n(a) Rick and Morty\n(c) The Simpsons\n(d) SpongeBob SquarePants\nAnswer: "
]

questions2 = [
    Question(question_2prompts[0], "c"),
    Question(question_2prompts[1], "a"),
    Question(question_2prompts[2], "a"),
    Question(question_2prompts[3], "c"),
    Question(question_2prompts[4], "a"),
    Question(question_2prompts[5], "b"),
    Question(question_2prompts[6], "c"),
    Question(question_2prompts[7], "b"),
    Question(question_2prompts[8], "d"),
    Question(question_2prompts[9], "d"), " "
]


def run_EASYtest(questions2, q=None):

    global Q  #number of questions

    global play_points

    
    valid = False

    global question
    for question in questions2:
        print()
        print()


        if my_timer == '  00 min(s), 00 sec(s)':
            no_time_end(play_points)
            break
        #if the points is lower than 0 it will end
        elif play_points <= 0:
            no_points_end(play_points)
            break
        elif question == questions2[10] and play_points > 0:
            time.sleep(0.7)
            print(
                "\n\nCongratulations! You have answered all questions. Your remaining points was '{}' and the amount of time left was '{}' "
                .format(play_points, my_timer))
            break

        else:
            answer = input(question.prompt).lower()

        #This code is for "no input" by user which is a loop for user to input something before they can continue
        if answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("******Please type in the alphabelts********")
            print()
            while not valid:
                answer = input(question.prompt).lower()

                if answer != "a" and answer != "b" and answer != "c" and answer != "d":
                    print("******Please type in the alphabelts********")
                    print()
                    valid = False
                elif answer == question.answer:
                    output_statement(
                        "  Correct answer! Points: " + str(play_points) +
                        str(x) + "Time left: " + str(my_timer), "#")
                    Q += 1
                    break
                else:
                    play_points -= 30
                    output_statement(
                        "   Wrong answer. Points: " + str(play_points) + str(x)
                        + "Time left: " + str(my_timer), "*")
                    Q += 1
                    break
        elif answer == "":
            print("Please type something.")
            print()
            while not valid:
                answer = input(question.prompt).lower()

                if answer == "":
                    print("Please type something.")
                    print()
                    valid = False
                elif answer != "a" and answer != "b" and answer != "c" and answer != "d":
                    print("Please type in the alphabelts")
                    valid = False
                elif answer == question.answer:
                    output_statement(
                        "  Correct answer! Points: " + str(play_points) +
                        str(x) + "Time left: " + str(my_timer), "#")
                    Q += 1
                    break
                else:
                    play_points -= 30
                    output_statement(
                        "   Wrong answer. Points: " + str(play_points) + str(x)
                        + "Time left: " + str(my_timer), "*")
                    Q += 1
                    break

        elif answer == question.answer:
            output_statement(
                "  Correct answer! Points: " + str(play_points) + str(x) +
                "Time left: " + str(my_timer), "#")
            Q += 1
        else:
            play_points -= 30
            output_statement(
                "   Wrong answer. Points: " + str(play_points) + str(x) +
                "Time left: " + str(my_timer), "*")
            Q += 1
    return


##MEDIUM QUESTIONS##
question_3prompts = [
    "What is the chemical symbol for silver? \n(a) Gc\n(b) Si\n(c) Ag\n(d) None of the above\nAnswer: ",
    "What year did the Titanic sink in the Atlantic Ocean on 15 April, on its maiden voyage from Southampton?\n(a) 1912\n(b) 1900\n(c) 1899\nAnswer: ",
    "What is the name of the biggest technology company in South Korea?\n(a) POSCO\n(b) Samsung\n(c) Kia Motors\n(d) All of the Above\nAnswer: ",
    "What is the capital of Portugal?\n(a) Cape Verde\n(b) Lisbon\n(c) Porto\n(d) Braga\nAnswer: ",
    "What is the world’s smallest bird?\n(a) Bee Hummingbird\n(b) Diamond Firetail\nAnswer: ",
    "What is the lifespan of a dragonfly?\n(a) 3years\n(b) 24hrs\n(c) 1year\n(d) 4months\nAnswer: ",
    "How many breaths does the human body take daily?\n(a) 20,000 daily\n(b) 10,000\n(c) 50,000\nAnswer: ",
    "In which year was The Godfather first released?\n(a) 1950\n(b) 1990\n(c) 1972\n(d) 1980\nAnswer: ",
    "How many hearts does an Octopus Have?\n(a) 4\n(b) 8\n(c) 2\n(d) 3\nAnswer: ",
    "Which country can the Colosseum be found?\n(a) France\n(b) Germany\n(c) Europe\n(d) Italy\nAnswer: "
]

questions3 = [
    Question(question_3prompts[0], "c"),
    Question(question_3prompts[1], "a"),
    Question(question_3prompts[2], "d"),
    Question(question_3prompts[3], "b"),
    Question(question_3prompts[4], "a"),
    Question(question_3prompts[5], "b"),
    Question(question_3prompts[6], "a"),
    Question(question_3prompts[7], "c"),
    Question(question_3prompts[8], "d"),
    Question(question_3prompts[9], "d"), " "
]


def run_MEDIUMtest(questions3, q=None):

    global Q  #number of questions

    global play_points
    global my_timer
    valid = False

    global med_play_points
    med_play_points = play_points * 2

    global question
    for question in questions3:
        print()
        print()

        if my_timer == '  00 min(s), 00 sec(s)' or '  00 sec(s)':
            no_time_end(med_play_points)
            break
        #if the points is lower than 0 it will end
        elif med_play_points <= 0:
            no_points_end(med_play_points)
            break
        elif question == questions3[10] and med_play_points > 0:
            time.sleep(0.7)
            print(
                "\n\nCongratulations! You have answered all questions. Your remaining points was '{}' and the amount of time left was '{}' "
                .format(med_play_points, my_timer))
            break

        else:
            answer = input(question.prompt).lower()

        #This code is for "no input" by user which is a loop for user to input something before they can continue
        if answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("******Please type in the alphabelts********")
            print()
            while not valid:
                answer = input(question.prompt).lower()

                if answer != "a" and answer != "b" and answer != "c" and answer != "d":
                    print("******Please type in the alphabelts********")
                    print()
                    valid = False
                elif answer == question.answer:
                    output_statement(
                        "  Correct answer! Points: " + str(med_play_points) +
                        str(x) + "Time left: " + str(my_timer), "#")
                    break
                    Q += 1
                else:
                    med_play_points -= 80
                    output_statement(
                        "   Wrong answer. Points: " + str(med_play_points) +
                        str(x) + "Time left: " + str(my_timer), "*")
                    Q += 1
                    break
        elif answer == "":
            print("Please type something.")
            print()
            while not valid:
                answer = input(question.prompt).lower()

                if answer == "":
                    print("Please type something.")
                    print()
                    valid = False
                elif answer != "a" and answer != "b" and answer != "c" and answer != "d":
                    print("Please type in the alphabelts")
                    valid = False
                elif answer == question.answer:
                    output_statement(
                        "  Correct answer! Points: " + str(med_play_points) +
                        str(x) + "Time left: " + str(my_timer), "#")
                    Q += 1
                    break
                else:
                    med_play_points -= 80
                    output_statement(
                        "   Wrong answer. Points: " + str(med_play_points) +
                        str(x) + "Time left: " + str(my_timer), "*")
                    Q += 1
                    break

        elif answer == question.answer:
            output_statement(
                "  Correct answer! Points: " + str(med_play_points) + str(x) +
                "Time left: " + str(my_timer), "#")
            Q += 1
        else:
            med_play_points -= 80
            output_statement(
                "   Wrong answer. Points: " + str(med_play_points) + str(x) +
                "Time left: " + str(my_timer), "*")
            Q += 1
    return


### HARD QUESTIONS ###
question_3prompts = [
    "How many stars does the New Zealand flag have? \n(a) 6\n(b) 7\n(c) 8\n(d) 9\nAnswer: ",
    "According to Maori legend the leader of the Maori expedition from Hawaiki that found Aotearoa was?\n(a) Kupe\n(b) Maui\n(c) Hone Heke\n(d) Te Kooti\nAnswer: ",
    "What does Aotearoa mean?\n(a) LAnd of the Long Bright Cloud\n(b) Our Place\n(c) Land of the Long White Cloud\n(d) Land of the Clouds\nAnswer: ",
    "What is the capital city of Paraguay?\n(a) Cape Verde\n(b) Lisbon\n(c) Asuncion\n(d) Braga\nAnswer: ",
    "In which country is the Troi-Rivieres bridge?\n(a) Canada\n(b) London\nAnswer: ",
    "At which hospital did the first heart transplant take place?\n(a) Groote Schuur Hospital\n(b) Waitakere Hospital\n(c) Carnavon Private Hospital\n(d) Waimarino\nAnswer: ",
    "So far, which continent has hosted the Olympics the most times?\n(a) Japan\n(b) North American\n(c) South America\n(d) Europe\nAnswer: ",
    "A “crepuscular” animal becomes active at what time?\n(a) Morning\n(b) Midnight\n(c) Afternoon\n(d) Dusk\nAnswer: ",
    "Christmas in New Zealand is in which season?\n(a) Winter\n(b) Autumn\n(c) Spring\n(d) Summer\nAnswer: ",
    "What was the first movie to be rated PG-13?\n(a) Red Dawn\n(b) Unhinged\n(c) This Town\n(d) Military Wives\nAnswer: "
]

questions4 = [
    Question(question_3prompts[0], "c"),
    Question(question_3prompts[1], "a"),
    Question(question_3prompts[2], "c"),
    Question(question_3prompts[3], "c"),
    Question(question_3prompts[4], "a"),
    Question(question_3prompts[5], "a"),
    Question(question_3prompts[6], "d"),
    Question(question_3prompts[7], "d"),
    Question(question_3prompts[8], "d"),
    Question(question_3prompts[9], "a"), " "
]


def run_HARDtest(questions4, q=None):

    global Q

    global play_points

    global hard_play_points
    hard_play_points = play_points * 5  #number of questions

    global my_timer

    valid = False

    global question
    for question in questions4:
        print()
        print()

        if my_timer == '  00 sec(s)':
            no_time_end(hard_play_points)
            break
        #if the points is lower than 0 it will end
        elif hard_play_points <= 0:
            no_points_end(hard_play_points)
            break
        elif question == questions4[10] and hard_play_points > 0:
            time.sleep(0.7)
            print(
                "\n\nCongratulations! You have answered all questions. Your remaining points was '{}' and the amount of time left was '{}' "
                .format(hard_play_points, my_timer))
            break

        else:
            answer = input(question.prompt).lower()

        #This code is for "no input" by user which is a loop for user to input something before they can continue
        if answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("******Please type in the alphabelts********")
            print()
            while not valid:
                answer = input(question.prompt).lower()

                if answer != "a" and answer != "b" and answer != "c" and answer != "d":
                    print("******Please type in the alphabelts********")
                    print()
                    valid = False
                elif answer == question.answer:
                    output_statement(
                        "  Correct answer! Points: " + str(hard_play_points) +
                        str(x) + "Time left: " + str(my_timer), "#")
                    Q += 1
                    break
                else:
                    hard_play_points -= 180
                    output_statement(
                        "   Wrong answer. Points: " + str(hard_play_points) +
                        str(x) + "Time left: " + str(my_timer), "*")
                    Q += 1
                    break
        elif answer == "":
            print("******Please type something.******")
            print()
            while not valid:
                answer = input(question.prompt).lower()

                if answer == "":
                    print("******Please type something.******")
                    print()
                    valid = False
                elif answer != "a" and answer != "b" and answer != "c" and answer != "d":
                    print("******Please type in the alphabelts******")
                    valid = False
                elif answer == question.answer:
                    output_statement(
                        "  Correct answer! Points: " + str(hard_play_points) +
                        str(x) + "Time left: " + str(my_timer), "#")
                    Q += 1
                    break
                else:
                    hard_play_points -= 180
                    output_statement(
                        "   Wrong answer. Points: " + str(hard_play_points) +
                        str(x) + "Time left: " + str(my_timer), "*")
                    Q += 1
                    break

        elif answer == question.answer:
            output_statement(
                "  Correct answer! Points: " + str(hard_play_points) + str(x) +
                "Time left: " + str(my_timer), "#")
            Q += 1
        else:
            hard_play_points -= 180
            output_statement(
                "   Wrong answer. Points: " + str(hard_play_points) + str(x) +
                "Time left: " + str(my_timer), "*")
            Q += 1
    return


######## LEVEL1 QUESTIONS ##########
def Level1start():
    time.sleep(0.5)
    print("\n\n\n\n\n")
    print("Level 1 Questions")
    time
    time.sleep(2)
    run_test(questions)

    ###### Displaying modes ########
    mode_run()
    #loop through response from user about what mode they choose
    valid = True
    while valid:

        error = "***   Whoops, type it again   ***"

        response = input("\n\nWhich Mode do you prefer? ").upper()

        if response == "EASY" or response == "E" or response == "1":
            print("ACCEPTED")
            print("\n\n\n\n\nLevel 2 Questions")
            time.sleep(1)
            countdown_thread = threading.Thread(target=countdown, args=[90])
            countdown_thread.start()
            run_EASYtest(questions2)
            break

        elif response == "MEDIUM" or response == "M" or response == "2":
            print("ACCEPTED")
            print("\n\n\n\n\nLevel 2 Questions")
            time.sleep(1)
            countdown_thread = threading.Thread(target=countdown, args=[60])
            countdown_thread.start()
            run_MEDIUMtest(questions3)
            break

        elif response == "HARD" or response == "H" or response == "3":
            print("ACCEPTED")
            print("\n\n\n\n\nLevel 2 Questions")
            countdown_thread = threading.Thread(target=countdown, args=[30])
            countdown_thread.start()
            run_HARDtest(questions4)
            break

        else:
            print(error)
            print()


###############################################################

######### INTRODUCTION  ###########
keep_going = ""
while keep_going == "":
    username = input("What is your name? ").upper()

    if username != keep_going:
        print()
        print()
        print("Hello " + username)
        break

    else:
        print("***Sorry, you have to type in your name!***")
time.sleep(1)
######################################################

#Starting level 1 questions
intro_counter(1)
Level1start()

#end game
play_again = input("\n\nPress <enter> to play again or any key to quit: ")

keep_going = ""
valid = False

while not valid:
    if play_again == keep_going:
        intro_counter(1)
        Level1start()
        valid = True
    else:
        animated_txt(message)
        valid = True
