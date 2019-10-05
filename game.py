'''game: text based escape'''

#this could be helpful in the future:
#https://github.com/typedeaf/text-adventure-tut


import time
import random
import os

#####
#utilities

DOOR_OPEN = False

PLAYER_NAME = []
PLAYER_LIFE = ['<3', '<3', '<3']
HP = ['<3', '<3', '<3']
INV = []

PLAYER_INFO = {
    'player name' : PLAYER_NAME,
    'player life' : PLAYER_LIFE,
    'inventory' : INV
}

def selectchoice(rules_choice):
    '''the player selection'''
    choice = input('>>>')
    if choice in rules_choice:
        return choice
    elif choice == 'quit':
        print('thanks for playing!')
        print('you can hit enter to close the game')
        input()
        #exit(0) <- this closes the window as soon as 'quit' it sent
    elif choice == 'restart':
        restart()
    elif choice == 'info':
        print(PLAYER_INFO)
        return selectchoice(rules_choice)
    elif choice == 'help':
        help()
        return selectchoice(rules_choice)
    else:
        print('invalid entry')
        return selectchoice(rules_choice)

#####
#introductory stuff


def start():
    '''beginning of the game'''
    name = input('State your name, player.\n>>>')
    PLAYER_NAME.append('{}'.format(name))
    print('Welcome to the game, {}.'.format(name))
    print('I\'m the narrator and I will be telling your story here.')
    print('Do you need the rules?')
    print('1. yes\n2. no')

    rules_choice = ['1', '2']
    choice = selectchoice(rules_choice)

    if choice == '1':
        print('\nHere are the basic rules.')
        rules()
        time.sleep(10)
        beginning()

    elif choice == '2':
        print('\nLet\'s begin then.')
        beginning()


def rules():
    '''the rules of the game'''
    print('Your objective is to escape the house without losing all your lives.')
    print('At every obstacle you will recieve choices.')
    print('In order to select choices enter the corresponding number.')
    print('Use the command "help" for more information.')

#####
#starting the game


def beginning():
    '''first thing to handle'''
    print('\nYou wake up, finding yourself in a dark room.')
    print('Getting up and feeling around, you find a light switch on the wall and turn it on.')
    print('You find that there are two doors on either side of you. \nWhat would you like to do?')
    print('1. go through the left door')
    print('2. go through the right door')

    door_choice = ['1', '2', str('dead')]
    choice = selectchoice(door_choice)

    if choice == '1':
        print('\nYou begin to head through the door to the left.')
        time.sleep(2)
        corridor()

    elif choice == '2':
        print('\nYou begin to head through the door to the right')
        time.sleep(2)
        dark_hall()

    elif choice == str('dead'):
        print('I\'m gunna kms lol')
        time.sleep(1)
        PLAYER_LIFE.remove('<3')
        PLAYER_LIFE.remove('<3')
        PLAYER_LIFE.remove('<3')
        if not PLAYER_LIFE:
            dead()
        else:
            print('didn\'t work, dude.')
            input()


def beginning_return():
    '''paste all beginning stuff here and change introductory text'''
    print('\nYou\'ve returned to the first room.')
    print('What would you like to do?')
    print('1. go through the left door')
    print('2. go through the right door')

    door_choice = ['1', '2']
    choice = selectchoice(door_choice)

    if choice == '1':
        print('\nYou begin to head through the door to the left.')
        time.sleep(2)
        corridor()

    elif choice == '2':
        print('\nYou begin to head through the door to the right.')
        time.sleep(2)
        dark_hall()

#####
#corridor stuff


def corridor():
    '''corridor that leads to __2 rooms__ and kitchen'''
    print('The doorway led to a long corridor.')
    time.sleep(2)
    print('\nThere are two doors at either side of you.')
    print('The end of the corridor opens up to what looks like a kitchen.\nWhat do you do?')
    print('1. go back')
    print('2. check the door to the right')
    print('3. check the door to the left')
    print('4. check the kitchen')

    corridor_choice = ['1', '2', '3', '4']
    choice = selectchoice(corridor_choice)

    if choice == '1':
        print('\nYou head back to the previous room.')
        time.sleep(2)
        beginning_return()

    elif choice == '2':
        print('\nYou head towards the room on the right side of the corridor')
        time.sleep(1)
        corridor_right_room()

    elif choice == '3':
        print('\nYou head towards the room on the left side of the corridor')
        time.sleep(1)
        corridor_left_room()

    elif choice == '4':
        print('\nYou walk down the corridor towards the kitchen.')
        time.sleep(2)
        kitchen()


def corridor_return():
    '''paste all corridor stuff here and change introductory text'''
    print('\nThe same two rooms are at either side of you.')
    print('Also that kitchen seems to welcome you towards it.')
    print('The door at the far end of the corridor is still left agape.')
    print('What do you do?')
    print('1. go back')
    print('2. check the door to the right')
    print('3. check the door to the left')
    print('4. check the kitchen')

    corridor_return_choice = ['1', '2', '3', '4']
    choice = selectchoice(corridor_return_choice)

    if choice == '1':
        print('\nYou head back to the previous room.')
        time.sleep(2)
        beginning_return()

    elif choice == '2':
        print('\nYou head towards the room on the right side of the corridor')
        time.sleep(1)
        corridor_right_room()

    elif choice == '3':
        print('\nYou head towards the room on the left side of the corridor')
        time.sleep(1)
        corridor_left_room()

    elif choice == '4':
        print('\nYou walk down the corridor towards the kitchen.')
        time.sleep(2)
        kitchen()

def corridor_right_room():
    #create boolean to make it recognize an open door
    #make an if statement to recognize an open or closed door
    print('The door is locked tight.')
    print('what do you do?')
    print('1. try and break it down')
    print('2. ignore it')

    right_door_choice = ['1', '2']
    choice = selectchoice(right_door_choice)
    if choice == '1':
        try:
            INV.index('crowbar')

        except ValueError:
            print('\nSeems the only way to open it is to force it open.')
            time.sleep(2)
            print('You kicked and banged at the door for a good while but it didn\'t move')
            print('You give up after a while and head back to the corridor.')
            time.sleep(2)
            corridor_return()

        else:
            DOOR_OPEN = True
            print('\nYou think that the crowbar would be useful in opening the door.')
            print('positioning the crowbar to open the door you being pulling for a while.')
            time.sleep(4)
            print('It worked! The door is open!')
            time.sleep(2)
            print('Unfortunatly the only thing behind it is a wall of laid bricks.')
            time.sleep(1)
            print('Who would even make a door that lead to a wall?')
            print('Frustrated, you return to the corridor.')
            corridor_return()

    elif choice == '2':
        print('\nYou decide to ignore the locked door.')
        print('You go back to considering choices in the corridor.')
        time.sleep(1)
        corridor_return()

def corridor_right_room_return():
    print('\nThat locked door is still standing there, still locked.')
    print('Still pretty mysterious.')
    print('What do you do?')
    print('1. force it open')
    print('2. ignore it')

    right_door_choice = ['1', '2']
    choice = selectchoice(right_door_choice)
    if choice == '1':
        try:
            INV.index('crowbar')

        except ValueError:
            print('\nSeems the only way to open it is to force it open.')
            time.sleep(2)
            print('You kicked and banged at the door for a good while but it didn\'t move')
            print('You give up after a while and head back to the corridor.')
            time.sleep(2)
            corridor_return()

        else:
            DOOR_OPEN = True
            print('\nYou think that the crowbar would be useful in opening the door.')
            print('positioning the crowbar to open the door you being pulling for a while.')
            time.sleep(4)
            print('It worked! The door is open!')
            time.sleep(2)
            print('Unfortunatly the only thing behind it is a wall of laid bricks.')
            time.sleep(1)
            print('Who would even make a door that lead to a wall?')
            print('Frustrated, you return to the corridor.')
            corridor_return()

    elif choice == '2':
        print('\nYou decide to ignore the locked door.')
        print('You go back to considering choices in the corridor.')
        time.sleep(1)
        corridor_return()


def corridor_left_room():
    '''left room of the corridor, crowbar aquisation abd monster encounter'''
    print('You walk into the room but can\'t see a thing since it\'s pitch black in there.')
    time.sleep(3)
    try:
        INV.index('candle')

    except ValueError:
        print('\nYou decide to leave, not wanting to risk hurting yourself in the dark.')
        time.sleep(2)
        corridor_return()

    else:
        print('\nLuckily you have that candle from earlier and use it to check the room.')
        print('You\'re able to see the general layout of the room through the dim light.')
        print('After looking around for a bit you notice a bed in the corner of the room.')
        print('You also see a dresser at the opposite end of the room.')
        print('What would you like to do?')
        print('1. go back to the corridor')
        print('2. check the bed')
        print('3. check the dresser')

        left_room_choice = ['1', '2', '3']
        choice = selectchoice(left_room_choice)

        if choice == '1':
            print('\nYou decide to leave the room.')
            time.sleep(2)
            corridor_return()

        elif choice == '2':
            print('\nYou walk towards the bed, as you get closer it looks less comfortable.')
            print('Because of this laying down seems less appealing.')
            print('However you consider looking under the bed.')
            time.sleep(1)
            print('But there could be monsters under there.')
            print('Considering this, what do you do?')
            print('1. lay on the bed anyway')
            print('2. look under the bed')
            print('3. go back to checking the room')

            bed_choice = ['1', '2', '3']
            choice = selectchoice(bed_choice)

            if choice == '1':
                print('\nYou decide you\'re too tired to care about the state of the bed.')
                print('You lay down on the bed and begin to drift off to sleep.')
                time.sleep(3)
                #import random for this
                monster_spawn = random.randint(1, 2)
                if monster_spawn == 1:
                    PLAYER_LIFE.remove('<3')
                    print('\nYou\'re suddenly awakened by a squeezing sensation.')
                    print('Panicked you look around seeing yourself wrapped by a tenticle.')
                    print('It seems to be coming from under the bed, there\'s no way to get away')
                    print('You feel the life being drained from you.')
                    if not PLAYER_LIFE:
                        dead()
                    else:
                        print('As suddenly as it came the tenticle vanished under the bed.')
                        print('Let\'s not do that again.')
                        print(PLAYER_LIFE)
                        corridor_left_room_return()

                else:
                    time.sleep(2)
                    print('\nAfter soem time you wake up feeling somewhat less tired.')
                    corridor_left_room_return()

            elif choice == '2':
                print('\nYou decide to check under the bed and see if you find anything useful.')
                print('Kneeling down you pull the covers up and look under')
                monster_spawn = random.randint(1, 4)
                if monster_spawn == '1':
                    PLAYER_LIFE.remove('<3')
                    print('\nImmedatly after looking under you\'re greeted by a mass of tenticles.')
                    print('The creature grabs you and squeezez tightly.')
                    print('You begin having trouble breathing as you try to fend off the monster.')
                    if not PLAYER_LIFE:
                        print('You begin to feel lightheaded and faint.')
                        dead()
                    else:
                        print('Suddenly the monster vanishes and you\'re left breathing heavily.')
                        print('You soon pick yorself up and continue wondering the room.')
                        print(PLAYER_LIFE)
                        corridor_left_room_return()

                elif monster_spawn == '2' or '3' or '4':
                    time.sleep(2)
                    print('\nYou don\'t find anything under the bed apart from some dust and lint.')
                    print('You get up and return to the center of the room.')
                    time.sleep(2)
                    corridor_left_room_return()

            elif choice == '3':
                print('\nYou decide there isn\'t anything worth checking around the bed.')
                corridor_left_room_return()

        elif choice == '3':
            print('\nYou decide to check the dresser to see if there could be anything useful.')
            time.sleep(2)
            print('Upon closer inspection the dresser is broken and coated in dust')
            print('Some of the drawers seem to be broken as well.')
            print('what do you do?')
            print('1. search the dresser')
            print('2. go back to checking the room')

            dresser_choice = ['1', '2']
            choice = selectchoice(dresser_choice)

            if choice == '1':
                INV.append('crowbar')
                print('\nYou decide to search the dresser')
                time.sleep(2)
                print('After some difficulty you\'re able to search most of the drawers.')
                print('You were able yo find a crowbar inside one of the more stuck drawers.')
                print('! crowbar added to inventory !')
                corridor_left_room_return()

            elif choice == '2':
                print('\nYou decide that checking the dresser is more trouble than it\'s worth.')
                time.sleep(2)
                corridor_left_room_return()


def corridor_left_room_return():
    '''returning to the corridor's left room'''
    print('\nYou return to the center of the room with the candle flickering slightly.')
    print('The bed and dresser are still in their respected places.')
    print('What do you do?')
    print('1. go back to the corridor')
    print('2. check the bed')
    print('3. check the dresser')

    left_room_choice = ['1', '2', '3']
    choice = selectchoice(left_room_choice)

    if choice == '1':
        print('\nYou decide to leave the room.')
        time.sleep(2)
        corridor_return()

    elif choice == '2':
        print('\nYou walk towards the bed, as you get closer it looks less comfortable.')
        print('Because of this laying down seems less appealing.')
        print('However you consider looking under the bed.')
        time.sleep(1)
        print('But there could be monsters under there.')
        print('Considering this, what do you do?')
        print('1. lay on the bed anyway')
        print('2. look under the bed')
        print('3. go back to checking the room')

        bed_choice = ['1', '2', '3']
        choice = selectchoice(bed_choice)

        if choice == '1':
            print('\nYou decide you\'re too tired to care about the state of the bed.')
            print('You lay down on the bed and begin to drift off to sleep.')
            time.sleep(3)
            #import random for this
            monster_spawn = random.randint(1, 2)
            if monster_spawn == 1:
                PLAYER_LIFE.remove('<3')
                print('\nYou\'re suddenly awakened by a squeezing sensation.')
                print('Panicked you look around seeing yourself wrapped by a tenticle.')
                print('It looks like it\'s cominf from under the bed, there\'s no way to get away')
                print('You feel the life being drained from you.')
                if not PLAYER_LIFE:
                    dead()
                else:
                    print('As suddenly as it came the tenticle vanished under the bed.')
                    print('Let\'s not do that again.')
                    print(PLAYER_LIFE)
                    corridor_left_room_return()

            else:
                time.sleep(2)
                print('\nAfter soem time you wake up feeling somewhat less tired.')
                corridor_left_room_return()

        elif choice == '2':
            print('\nYou decide to check under the bed and see if you find anything useful.')
            print('Kneeling down you pull the covers up and look under')
            monster_spawn = random.randint(1, 4)
            if monster_spawn == '1':
                PLAYER_LIFE.remove('<3')
                print('\nImmedatly after looking under you\'re greeted by a mass of tenticles.')
                print('The creature grabs you and squeezez tightly.')
                print('You begin having difficulty breathing when you try to fend off the monster.')
                if not PLAYER_LIFE:
                    print('You begin to feel lightheaded and faint.')
                    dead()
                else:
                    print('Suddenly the monster vanishesand you\'re left breathing heavily.')
                    print('You soon pick yorself up and continue wondering the room.')
                    print(PLAYER_LIFE)
                    corridor_left_room_return()

        elif choice == '3':
            print('\nYou decide there isn\'t anything worth checking around the bed.')
            corridor_left_room_return()

    elif choice == '3':
        print('\nYou decide to check the dresser to see if there could be anything useful in it.')
        time.sleep(2)
        print('Upon closer inspection the dresser is broken and coated in dust')
        print('Some of the drawers seem to be broken as well.')
        print('what do you do?')
        print('1. search the dresser')
        print('2. go back to checking the room')

        dresser_choice = ['1', '2']
        choice = selectchoice(dresser_choice)

        if choice == '1':
            time.sleep(1)
            print('\nThere isn\'t anything new in the dresser.')
            print('You decide to go back to the middle of the room.')
            corridor_left_room_return()

        elif choice == '2':
            print('\nYou decide that checking the dresser is more trouble than it\'s worth.')
            time.sleep(2)
            corridor_left_room_return()


def kitchen():
    '''the kitchen, possible weapon, cheat win'''
    print('\nThe kitchen is lit well enough to not need another light source.')
    print('Although it seems to have been left in shambles.')
    print('There is dust everywhere and every chair is overturned.')
    print('Most of the cabinets are ledt open and seem to be empty as well.')
    print('What do you do?')
    print('1. go back to the corridor')
    print('2. check the cabinets')

    kitchen_choice = ['1', '2', str('sandwich')]
    choice = selectchoice(kitchen_choice)

    if choice == '1':
        print('\nYou decide that the kitchen isn\'t worth your time and leave.')
        time.sleep(2)
        corridor_return()

    elif choice == '2':
        INV.append('old knife')
        print('\nYou begin searching through the kitchen for anything worthwhile.')
        time.sleep(3)
        print('apart from various, oddly still fresh, food items you find an old knife.')
        print('! old knife added to inventory !')
        print('You go back to the middle of the kitchen.')
        time.sleep(1)
        kitchen_return()

    elif choice == str('sandwich'):
        print('\nYou decide that you\'re hungry and want to make yourself some food.')
        print('It just so happens that there\'s just enough food in here to make a nice sandwich.')
        time.sleep(1)
        print('After looking some more you find a fresh tomato and some lettuce.')
        time.sleep(3)
        print('Oh? What\'s this?')
        time.sleep(1)
        print('There were some pickles too.')
        time.sleep(2)
        print('This sandwichis going to come out quite nicely.')
        time.sleep(5)
        print('After making the sandwich you pick up one of the chairs and take a seat.')
        print('Taking a bite out of the sandwich feels good enough to make you win the game.')
        time.sleep(3)
        win()


def kitchen_return():
    '''going back to the kitchen'''
    print('\nBack in the middle of the kitchen you weigh your options.')
    print('The cabinets are still there but not much else.')
    print('What do you do?')
    print('1. go back to the corridor')
    print('2. check the cabinets')

    kitchen_choice = ['1', '2', str('sandwich')]
    choice = selectchoice(kitchen_choice)

    if choice == '1':
        print('\nYou decide that the kitchen isn\'t worth your time and you leave.')
        time.sleep(2)
        corridor_return()

    elif choice == '2':
        print('\nYou search the kitchen for anything else you could have missed.')
        time.sleep(3)
        print('\nStill just some weirdly fresh foods.')
        print('No use checking for anything else.')
        time.sleep(1)
        kitchen_return()

    elif choice == str('sandwich'):
        print('\nYou decide that you\'re hungry and want to make yourself some food.')
        print('It just so happens that there\'s just enough food in here to make a nice sandwich.')
        time.sleep(1)
        print('After looking some more you find a fresh tomato and some lettuce.')
        time.sleep(3)
        print('Oh? What\'s this?')
        time.sleep(1)
        print('There were some pickles too.')
        time.sleep(2)
        print('This sandwichis going to come out quite nicely.')
        time.sleep(5)
        print('After making the sandwich you pick up one of the chairs and take a seat.')
        print('Taking a bite out of the sandwich feels good enough to make you win the game.')
        time.sleep(3)
        win()

#####
#dark hall stuff


def dark_hall():
    '''a dark hall leading to an enimy(?)'''
    print('\nYou enter a dark hallway, you can\'t even see your hand in front of your face.')
    print('You notice an unlit candle by your feet.')
    print('What would you like to do?')
    print('1. go back')
    print('2. pick up candle')

    candle_choice = ['1', '2', '420']
    choice = selectchoice(candle_choice)

    if choice == '1':
        print('\nYou left the candle and leave.')
        time.sleep(2)
        beginning_return()

    elif choice == '2':
        time.sleep(1)
        INV.append('candle')
        print('\nYou picked up the candle.')
        print('! candle added to inventory !')
        time.sleep(3)
        print('\nYou lit the candle and use the dim light to gather your bearings of the hall.')
        print('Would you like to continue down the hall?')
        print('1. yes')
        print('2. no, go back')

        dark_hall_choice = ['1', '2']
        choice = selectchoice(dark_hall_choice)

        if choice == '1':
            time.sleep(1)
            print('\nYou decide to continue down the hall.')
            print('After some time you hear a noise at the end of the hall.')
            print('You also see a door to the right.')
            print('What do you do?')
            print('1. check the noise')
            print('2. check the doorway to the right')
            print('3. go back')

            hall_choice = ['1', '2', '3']
            choice = selectchoice(hall_choice)

            if choice == '1':
                time.sleep(2)
                print('\nYou decide to continue down the hall to check the noise.')
                print('The flickering light of the candle is your only source of light as you wonder towards the noise.')
                print('The closer you get to the noise the more frightening it seems to be.')
                print('After getting closer you begin to think it sounds vaguely like a person in pain.')
                time.sleep(3)
                print('Finally you reach a door at the end of the hall.')
                print('The sound of what you believe to be a person in agony develops into a houling scream.')
                print('You get second thoughts of checking the room.')
                print('but they may need your help.')
                print('What do you do?')
                print('1. check the room, they need you')
                print('2. go back, the entire thing is frightening')

                man_choice = ['1', '2']
                choice = selectchoice(man_choice)

                if choice == '1':
                    print('\nYou decide to disregard any fears and check the room.')
                    print('There could be someone in need in there.')
                    time.sleep(2)
                    man_room()
                
                elif choice == '2':
                    print('\nJudging by the looks of the rest of this place you decide this must be a trap.')
                    print('You leave the door and ignore the screams as you walk away.')
                    time.sleep(3)
                    dark_hall_return()


            ##finish stuff here##

        elif choice == '2':
            print('\nYou begin to head back to the last room.')
            time.sleep(2)
            beginning_return()

    elif choice == '420':
        print('\nYeah, blaze it broski')
        time.sleep(2)
        win()


def man_room():
    #put code for the man room here
    print('\nYou begin opening the door and pause half way.')
    print('The screaming stops immedatly and turns into a soft whimpering.')
    print('Determined, you open the door and walk into the room.')
    print('You look around and see a man curled into a ball in the far corner of the room.')
    print('Hesitantly, you approach to see if he is alright.')
    time.sleep(4)
    print('You look over him as he lays on the floor.')
    time.sleep(1)
    print('As quickly as the crying stopped the man got up.')
    time.sleep(1)
    print('The first things you notice about him are his sharpened teeth and sunken eyes.')
    time.sleep(1)
    print('Before you can react the man lunges at you.')
    print('You stumble back, falling onto the floor.')
    print('Panicing, you begin to scramble backwards across the floor the man approaches.')
    print('What do you do?')
    print('1. run!')
    print('2. fight')

    man_room_choice = ['1', '2']
    choice = selectchoice(man_room_choice)

    if choice == '1':
        #run away
        #take damage from man
        print('')

    elif choice == '2':
        #fight the man
        #make combat system using a range of random numbers for items and man attack power
        #no initial damage but can take damage during fight
        #reward for fighting man?
        print('')


#to be used after first introduction of dark_hall
def dark_hall_return():
    '''paste all dark_hall stuff here and edit from introductory text'''

    ##finish stuff here (paste from dark_hall and revise for appropreate progress)

#####
#utilities II


def help():
    print('\nHELP')
    rules()
    print('\nCOMMANDS')
    print('restart: restart the game')
    print('info: show all player info')
    print('quit: quit the game')

def restart():
    print('alrighty then, we restart in 3 seconds')
    time.sleep(3)
    reset()


def reset():
    '''for when a restart is mandatory'''
    os.system('cls')
    del PLAYER_LIFE[:]
    PLAYER_LIFE.extend(HP)
    del INV[:]
    print('! RESTARTED !')
    beginning()

def dead():
    '''for when the player dies in game'''
    print('\n\nyou died.')
    time.sleep(2)
    print('\nwanna try again?')
    print('1. yes')
    print('2. no')

    dead_choice = ['1', '2']
    choice = selectchoice(dead_choice)

    if choice == '1':
        print('alrighty, here we go.')
        time.sleep(2)
        reset()

    elif choice == '2':
        print('alrighty, gg')
        print('you can hit enter to close the game')
        input()


def win():
    '''for when a player wins the game'''
    print('\n\nYOU WIN!')
    time.sleep(2)
    print('\nwant to play again?')
    print('1. yes')
    print('2. no')

    win_choice = ['1', '2']
    choice = selectchoice(win_choice)

    if choice == '1':
        print('alrighty, here we go.')
        time.sleep(2)
        reset()

    elif choice == '2':
        print('alrighty, gg')
        print('you can hit enter to close the game')
        input()


#####


start()
