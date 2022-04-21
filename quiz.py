from PIL import Image #Used to be able to open images using the pillow library

question1 = Image.open('question1.jpeg') #These are variables which when called use the pillow library to open images
question2 = Image.open('question2.jpeg') 

def pictureQuestions(): #This function calls images using the pillow library
    global score

    question1.show()

    while True: #Shows the user an image of a question, then promts them to answer in the command line
        try:
            user_Input = int(input("What is the answer to that question?: "))
            if user_Input == 36:
                print("You got it right!") #If answer is correct their global score goes up, otherwise it doesn't
                score +=1
            else:
                print ("You got it wrong")
            break
        except: #Failsafe to ensure user inputs an integer
            print("Invalid input")


        while True: #Sees if the user wants to keep going 
            proceed = input("Do you want to continue?(yes/no)")
            if proceed.lower() == "yes":
                break
            elif proceed.lower() == "no":
                print("Thats too bad")
                results()
                return 0
            else:
                print("invalid input")

    question2.show() #Same image showing process as above

    while True:
        try:
            user_Input = int(input("What is the answer to that question?: "))
            if user_Input == 4:
                print("You got it right!")
                score +=1
            else:
                print ("You got it wrong")
            break
        except:
            print("Invalid input")

score = 0

total = 10

question_Bank = {"8 + 8 = " : 16, "17 + 2 = " : 19,\
     "4 + 5 = " : 9, "9 + 2 = " : 11, "4! = " : 24, "33 + 3 = " : 36, "7 * 5 = " : 35} #A dictionary with simple math problems

def quiz():

    global score

    questions_Asked = 0

    for questions in question_Bank: #For each key (question) in the disctionary, the user gets an input prompt \
        #asking a question. The user input is them compared with the answer (as an integer) to that question per question.

        questions_Asked += 1

        answer = question_Bank[questions] #Answer changes depending on the question key


        while True:

            try:
            
                user_Answer = int(input(questions))

                break

            except: #Ensures the user inputs an integer

                print("invalid input")

        print (f"Correct answer: {answer}")

        if user_Answer == answer: #compare user input with answer, gives point if correct
            print("You got it right!")
            score += 1

        else:
            print("You got it wrong :(")


        if len(question_Bank) == questions_Asked: #Once the dictionary is finished, the photo questions begin, after which results are given, then the quiz ends

            pictureQuestions()

            results()

            restart() 
            return 0

    
        while True: #Sees if the user wants to continue
            proceed = input("Do you want to continue?(yes/no)")
            if proceed.lower() == "yes":
                break
            elif proceed.lower() == "no":
                print("Thats too bad")
                results()
                return 0
            else:
                print("invalid input") #Ensures valid response is given

    

def results(): #Prints out results, using percents and total score from the global score variable the global total variable
    global total
    global score
    percent = score / total * 100
    print (f"You got {score} out of {total} correct")
    print (f'That is {percent}% correct')

def restart(): #Gives user the option to restart the game
    while True:
        restart = input("Do you want to re-take the quiz?(yes/no)")
        if restart.lower() == "yes":
            quiz()
        elif restart.lower() == "no":
            print("Thats too bad")
            break
        else:
            print("invalid input")

def begin(): #Starts the game if user wants to play
    while True:
        request = input("Do you want to play a game? (yes/no)")
        if request.lower() == "yes":
            quiz()
            break
        elif request.lower() == "no":
            print("Too bad")
            results()
            break
        else:
            print("Invalid input")

begin()
