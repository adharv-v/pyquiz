import time

def func_game_opening():
    print("Welcome to Guess The Doors. \n You will be given a series of doors to choose \n which, if answered correctly, will let you progress onto the next part of your EXCITING escape!")
    time.sleep(3)
    print("\n If a question is answered wrong you get to attempt it again.\n For all the questions questions, type either 'A', 'B', 'C' or 'D.")


def func_player_info():
    name = input("Before we start the game, lets get your player name. \n What will your player name be?")
    print()
    print("Okay background information \n 15 June 2017 \n You are",name,", a secret spy who works for the FBI \n You are trapped in Dr.Vertigo's evil laboratory \n You have to get out quickly" )

    

        


def question_1():   
    while True:        
        print("Your first challenge. \n You are stuck in the basement of a laboratory. You see three doors. \n Which do you choose: \n A) Has a hungry lion who hasn't eaten for months")  
        time.sleep(3)
        print("B) Has poisonous gas that will suffocate you ")
        time.sleep(1)
        print("C) Has a room full of lava which will burn you ")
        time.sleep(1)
        print("D) A cave full of poisonous spiders")
        time.sleep(1)
        qwerty = input("Which door do you choose?")        
        if qwerty == "A" : 
            print ("You got it correct!\n A lion which hasn't eaten in months would be dead.\n Move on to next question \n")
            break
        else:
            print("Wrong - try again")
            time.sleep(3)

        

def Story():
    print("You walk past the corpse of the lion and into a marble chamber. Again, you see three doors!")

def question_2():
    while True:        
        print("Your second challenge. \n Which do you choose: \n A) Has spikes which will impale you.")  
        time.sleep(3)
        print("B) Has an an angry spirit that will possess you ")
        time.sleep(1)
        print("C) Has a freshwater tank full of Megaladons ")
        time.sleep(1)
        print("D) A cave full of Carbon Monoxide.")
        time.sleep(1)
        qwerty = input("Which door do you choose?")        
        if qwerty == "C" : 
            print ("You got it correct!\n A Megalodon cannot survive in freshwater.\n Move on to next question \n")
            break
        else:
            print("Wrong - try again")
            time.sleep(3)

     
def story2():
    print("You enter the tank and swim through. You see four tunnels. You are running out of air. Which one do you choose?")


def question_3():
    while True:        
        print("Your third challenge. \n Which do you choose: \n A) Has hungry piranhas")  
        time.sleep(3)
        print("B) Has a giant basking shark ")
        time.sleep(1)
        print("C) Has a giant cave that implodes every ten seconds ")
        time.sleep(1)
        print("D) A mysterious portal")
        time.sleep(1)
        qwerty = input("Which door do you choose?")        
        if qwerty == "B" : 
            print ("You got it correct!\n A basking shark is harmless to humans.\n Move on to next question \n")
            break
        else:
            print("Wrong - try again")
            time.sleep(3)


def Adharv():
    print("You escape into a great hall.\n You are soaking wet.\n You see three portals. Which do you choose?")


def question_4():
    while True:        
        print("A) Has a wall of fire.")  
        time.sleep(1)
        print("B) Has an infinite abyss ")
        time.sleep(2)
        print("C) is a portal to the dinosaur times. ")
        time.sleep(2)
        print("D) Into a desert which reaches 100 degrees Celcius at night time and 300  at day time.")
        time.sleep(3)
        qwerty = input("Which door do you choose?")        
        if qwerty == "A" : 
            print ("You got it correct!\n Since you are soaking wet you somewhat have immunity to the fire.\n If you are quick enough you will be able to get throught the wall of fire unscathed\n Move on to next question \n")
            break
        else:
            print("Incorrect - You are so dumb. Why would you choose that?\nTry again!")
            time.sleep(4)

def alvin_and_the_chipmunks_rule():
    print("Beyond the wall of fire you see three cages with mutant animals. You have to fight one of them to get into the next room.\n Which do you choose?")


def question_5():
    while True:        
        print("A) Has a mix of a lion, hippo and rhinocerous.")  
        time.sleep(1)
        print("B) Has a crocodile and a tiger mixed into one")
        time.sleep(2)
        print("C) A pigeon and a T-rex. ")
        time.sleep(2)
        print("D) An alligator-shark hybrid in a tank full of water (Again. So booring!)")
        time.sleep(3)
        qwerty = input("Which hbrid do you choose?")        
        if qwerty == "D" : 
            print ("You got it right!\n A shark is a saltwater creature whle an alligator is a freshwater creature.\n Therefore, no matter what type of water the tank is full of, the creature will die!")
            break
        else:
            print("Incorrect - You are so dumb. Why would you choose to fight that?\n Try again!")
            time.sleep(4)


def question_6():
    while True:        
        print("A) Water")  
        time.sleep(1)
        print("B) Slime ")
        time.sleep(2)
        print("C) Cotton candy and popcorn ")
        time.sleep(2)
        qwerty = input("Which do you choose?")        
        if qwerty == "C" : 
            print ("You got it correct!\n Move on to next question \n")
            break
        else:
            print("Incorrect - You are so dumb. This is not Minecaft.\nTry again!")
            time.sleep(4)

def question_7():
    while True:        
        print("A) Guards that will shoot anyone on sight.")  
        time.sleep(1)
        print("B) A maniacal villager that can only let you pass if you feed them and their family.")
        time.sleep(2)
        print("C) A killer clown!")
        time.sleep(2)
        qwerty = input("Which do you choose?")        
        if qwerty == "B" : 
            print ("You got it correct!\n  Just use the tub of cotton candy and popcorn to feed them.\n Move on to next question \n")
            break
        else:
            print("Incorrect - You are so dumb.\n Do you WANT to DIE or what?\nTry again!")
            time.sleep(4)

def ligmaballs():
    while True:        
        print("A) your mom with your failed test and a belt")  
        time.sleep(1)
        print("B) A door leading to the famous volcano mount Vesuvius.")
        time.sleep(2)
        print("C) A cliff which leads into an endless abyss")
        time.sleep(2)
        qwerty = input("Which do you choose?")        
        if qwerty == "B" : 
            print ("You got it correct!\n  Mount vesuvius is a dormant/extinct volcano.\n")
            break
        else:
            print("Incorrect - You are so dumb.\n Do you WANT to get KILLED or what?\nTry again!")
            time.sleep(4)









func_game_opening()
time.sleep(5)
func_player_info()
time.sleep(5)
question_1()
time.sleep(3)
Story()
time.sleep(3)
question_2()
time.sleep(3)
story2()
time.sleep(4)
question_3()
time.sleep(3)
Adharv()
time.sleep(3)
question_4()
time.sleep(3)
alvin_and_the_chipmunks_rule()
time.sleep(4)
question_5()
time.sleep(3)
print(" You beat up the hybrid and a trap door opens beneath you into a dropper. You see three tunnels with different things to break your fall.\n Which do you choose")
question_6()
time.sleep(4)
print("In the room, you clamber out of the tub of movie snacks and see three doors which do you choose?")
time.sleep(3)
question_7()
print("He lets you pass. You see three doors. One of them could get you out of the complex.")
ligmaballs()
time.sleep(5)
print("CONGRATULATIONS! YOU HAVE BEATEN THE GAME!")



























































