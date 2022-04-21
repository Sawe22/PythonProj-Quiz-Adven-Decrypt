from PIL import Image #Allows images to be imported and opened

portal = Image.open("portal.jpeg") #The following are four images stored in variables

civilization = Image.open("civilization.jpeg")

bus = Image.open("bus.jpeg")

patient = Image.open("patient.jpeg")

choice = "" #Setting some global variables to blank strings

name = ""

def greeting(): #A function which asks the user for thier name and ensures that its not an integer

    global name #Makes it so this global variable is usable in the function

    while True:  #If the input is an integer, there is no error and the while loop repeats. If it is a string (A potential name) there is an error which breaks the while loop, and allows the name to fo through

        name = input("Please enter your name: ")

        try:

            print(f"{int(name)} is an Invalid name")

            
        except:

            break


def Bahamas(): #A function which pkays out the bahamas scenario
    
    global name #using the global name variable, as well as getting the global patient image variable to use in this function
    global patient #Makes it so this global variable is usable in the function
    
    print(f"{name}, You've entered a mysterious coconut hut in the Bahamas.")
    print("")

    while True: #The user is to choose between 3 choices, and cannot proceed unless a valid input is given

        choice1 = input("You noticed a mysterious lantern sitting on the roof of the hut. Do you go up to get it (1), do you ignore it and do a back flip (2), or do you freeze in terror due to the demonic entity you noticed lingering around the lantern(3)?: ")
        print("")
        if choice1 == "1" or choice1 == "2" or choice1 == "3":
            break
        else:
            print("Invalid input")

    if choice1 == "1":
        print("You broke your neck trying to climb up to get the potion and died. Try again next time")
        return 0 #The function ends if the user inputs "1"
    elif choice1 == "3":
        print("It was unwise of you to have reacted. The horrors which were to follow must not be shared with the souls of the innocent. Maybe another adventurer may walk this path to find success.... Try again next time. ")
    else:
        while True: #If the user chose a valid input that was not 1 or 3 (they chose 2), they can proceed to this while loop

            choice2 = input("Doing a backflip had you hit your head and you are now in a coma. When you awake, you notice an eerie figure staring at you from outside your hospital bed window. Do you ignore it (1), do you call a nurse to address your issue (2) or do you jump the entity(3)? ")
            print("")
            if choice2 == "1" or choice2 == "2" or choice2 == "3": #The user is to choose between 3 choices, and cannot proceed unless a valid input is given
                break
            else:
                print("Invalid input")
        if choice2 == "1":
            print("It was unwise of you to ignore the creature. It is now infuriated. The shock from what was to come put you back into a coma, permanently. Try again next time")
        elif choice2 == "2":
            print("The entity is insulted by your insolence. You have doomed both yourself and the poor nurse to an enternity of suffering")
        else:
            print("You pull out your glock and shoot the entity. It dies. Congragulations, you purged an ancient evil from our world!")         
            patient.show()  #if the user chooses a valid input thats not 1 or 2 (they chose 3), and image appears


def Forest():#A function which plays out the forest scenario

    global civilization #Allows for use of this global image variable in the function

    global name #Makes it so this global variable is usable in the function



    print("You've stumbled upon a tree trunk in an suspicious opening in the middle of a dense forest.")
    print("")

    while True: #Makes the user give an input until they give a valid one

        choice1 = input("You get a bad feeling about entering the opening, something is definitely watching you. Do you proceed regardless(1), do you turn back into the forest (2), or do you stop where you are to scan your environment?(3)?: ")
        print("")
        if choice1 == "1" or choice1 == "2" or choice1 == "3":
            break
        else:
            print("Invalid input")

    if choice1 == "1":
        print("You should have listened to your gut feeling. The opening was a trap for lost travelers wanting to find refuge for the night. You do not come home to tell the tale of what happened. Try again next time.")
        return 0 #if they choose 1, the function ends
    elif choice1 == "3":
        print("You stop to scan your environment. For a moment all seems wells until you notice something hidden up above in the branches a few trees down. As you inspect closer, the leaves start to rustle and as you notice that something is in the trees; it knows you see it. You come to realize that you are surrounded\
. You are never heard from again. Try again next time. ")
    else: #If the user chooses a valid input which is not 3 or 1 (they chose 2), they proceed to this while loop
        while True: #The user is to choose between 3 choices, and cannot proceed unless a valid input is given

            choice2 = input("You listened to your gut and turn away from the opening. There is still no sign of civilization, and you start to hear rulsting behind you. As the\
sound approahces, do you ignore it and continue normally (1), do you stop to investigate (2) or do you run for your life?(3)? ")
            print("")
            if choice2 == "1" or choice2 == "2" or choice2 == "3": 
                break
            else:
                print("Invalid input")
        if choice2 == "1":
            print("As you continue to walk normally, the sounds get closer and closer. You decide to break out into a run. It is too late. The creatures consume you")
        elif choice2 == "2":
            print("You stop to investigate. Promptly, you find your self face to face with unspeakable horrors. You do not come back to tell your tale. Try again next time. ")
        else: #If a valid non 1 or 2 input is given (if 3 is chosen) the user may win the game, and an image is displayed
            print(f"{name}, You run. The rustling grows further and further until it subsides completely. Regardless, you continue to run. You finally stuble upon civilization a few hours down the road. You will never know what those noises were..")
            civilization.show()


def Whalley():#A function which plays out the Whalley scenario

    global name #Makes it so this global variable is usable in the function

    global bus #Makes it so this global variable is usable in the function

    print("You've entered a school. Upon closer inspection you realize you are in Kwantlen Park Secondary.")
    print("")

    while True: #The user is to choose between 3 choices, and cannot proceed unless a valid input is given

        choice1 = input("The morning bell just rang! You don't know the block order! Do you go to your homeroom, (1), do you go home (2), or do you go to the office(3)?: ")
        print("")
        if choice1 == "1" or choice1 == "2" or choice1 == "3":
            break
        else:
            print("Invalid input")

    if choice1 == "1":
        print("You decide to head towards your homeroom. You are slightly annoyed to be at school and have some brain fog; you're really not in the mood to learn. You take a seat and start taking notes. You grow bored as your same old teacher goes on to teach\
thier same old boring lesson, you start to doze off. Suddenly, you are hit with a sharp sense of terror as you make a realization. You graduated 9 years ago. This teacher retired a few years back and the friends which now sit around you left your life a long time ago\
. The lightbulbs all suddenly pop and everyone's head jerks in your direction; contorting in unnatural ways. As you observe the fog now visable from being back lit by the eerie red glow emmited from the open mouthed jaws of your demonic peers, you chuckle to yourself;\
realizing your story will never be told. Try again next time.")

        return 0
    elif choice1 == "3":
        print("As you sit down in the office waiting for the secretary to come, the seconds ticks by. Seconds turn to minutes, which turn to an hour.\
. You realize that something must be wrong, so you head for the exit. However, you are greeted by a wall where the exit used to be. Terrified, you run around looking for someone to get you out\
; no one in sight. You spend the rest of your days trapped in the office; mocked by the inpenetrable windows showing a perpetual beautiful day outside. Try again next time.")
    else:
        while True: #If a valid input which is not 1 or 3 is given (2 is the input), the user may proceed to this while loop

            print("")

            choice2 = input("You decide to head home. Good thing too, as you just remembered how you graduated years ago. How awkward would it have been if you\
looked for your classes!? Still, it's off putting that you forgot for a moment how you are no longer a highschool student. You now approach your house, but an offputting sensation lingers...\
Do you ignore it and go home to sleep?(1) Do you knock on the door to see who's home?(2) Or do you wait outside for a while longer(3)? ")
            print("")
            if choice2 == "1" or choice2 == "2" or choice2 == "3": #The user is to choose between 3 choices, and cannot proceed unless a valid input is given
                break
            else:
                print("Invalid input")
        if choice2 == "1":
            print("You go home and look around for your family; no one is home. You figure they went out shopping so you go to sleep in your room.\
. Some time later you wake up. You find yourself in the ground in a dimly lit, 10m cube room with no light source. There are no windows, doors or exits, just\
 baige drywall all around. You realize you are trapped. You never leave the room. Try again next time")
        elif choice2 == "2":
            print("You knock on the door. You are met by your mother. You remember your mother passed away when you were in highschool. You scream. The entity screams louder. \
You are never heard from again. Please try again.")
        else: #If the user choses a valid input which is not 2 or 1 (They chose 3), they can survive, and an image of a bus comes up
            bus.show()
            print(f"{name}, You stand outside for something to happen; nothing does. You're finding it odd that there is no one on the roads, when you are hit with the sharp realization; You moved away from this house right after highschool; this isn't your home; it got\
 demolished ages ago to build new infrastructure. You realize this shouldn't be happening so you run in the opposite direction. After a few kilometers people start to appear and eventually you catch the skytrain to go back home.\
. You don't know what to think of this experiance and later convince yourself that it was all a dream. It had to be....")


def adventure_Path():#A function which plays out all other funtions based off of user input

    global portal #Makes it so this global variable is usable in the function

    global choice#Makes it so this global variable is usable in the function

    global name#Makes it so this global variable is usable in the function

    greeting() #Plays the greeting function

    portal.show() #Shows image of a portal

    while True: #Makes the user choose yes or no, until they give a valid input. The input is made to not be case sentitive as everything becomes lowe cased

        choice = input((f"Hello {name}. You stumble upon a mysterious portal. Do you wish to enter it?(yes/no): "))

        if choice.lower() == "no":

            print("That's too bad")

            return 0

        elif choice.lower() == "yes": #If the user choses yes, they can chose between the three scenarios. 

            while True:

                decision = input("The portable seems to fluctuate between three locations. Do you want to get into it as the Bahamas appear (1),\
 when you see a dense forest (2), or when you see Whalley (3)?: ") #The user must chose 1, 2, or 3 to call a function, or else the loop repeats
                
                if decision == "1":

                    Bahamas()

                    return 0

                elif decision == "2":

                    Forest()

                    return 0
                
                elif decision == "3":

                    Whalley()

                    return 0

                else:

                    print("Invalid Input")
        else: #If the user gave an invalid input, they must enter another input
            print("Invalid input")



adventure_Path() #Calls the function which can call all other functions
