name = "[placeholder]"

def done():
    print(" ")
    print("You have collected all the items Ulfric required. ")
    print("You make your way back to the control room.")
    print(" ")
    print("Ulfric says:")
    print("'Thank you so much for getting my stuff back!")
    print("Sorry for turning you into a 28 year old Russian male!'")
    print(" ")
    print(name, "says: ")
    print("'So you'll turn me back and send me home now?")
    print("I'm going to be late for work!'")
    print(" ")
    print("Ulfric says:")
    print("'Of course! Goodbye,", name, "'")
    return;

def capk():
    global arb
    global cap
    cap = 1

    print(" ")
    print("You enter the Captain's Room.")
    print("Do you look in the")
    print("1. Locker")
    print("2. Under the bed")
    capan = input(" ")
    if capan == "1":
        print("You look in the locker and find a golden sparkly gun.")
        if arb == 1:
            done()
        else:
            print(" ")
            print("You enter the remaining room.")
            armory()
    else:
        print("You look under the bed and an ALIEN jumps out. You get eaten.")
        dead()

def armcho():
    global cap
    global arb

    arm = input(" ")
    if arm == "1":
        print(" ")
        print("You go to look at the rifles, but an alien jumps out.")
        print("You get eaten and die!")
        dead()
    if arm == "2":
        print(" ")
        print("You look at the space suits and find a golden glittery one!")
        print(" ")
        if cap == 1:
            done()
        else:
            print("You go into the remaining room.")
            capk()
    else:
        armcho()

def armory():
    global arb
    global cap
    arb = 1
    print(" ")
    print("You enter the armory.")
    print("There is an ALIEN on the floor!")
    print(" ")
    print("1. Kill it!")
    print("2. Run!")
    ruki = input(" ")
    if ruki == "1":
        print("You shoot the alien and kill it. That was scary.")
        print(" ")
        print("Now it is time to explore the armory.")
        print("What do you look at?")
        print("1. Rack of laser rifles")
        print("2. Rack of space suits")
        armcho()
    else:
        print("You attempt to run, but slip in some alien juice.")
        print("The alien eats you.")
        dead()

def lol():
    global arb
    global cap
    arm = 0
    cap = 0
    nyo = input(" ")
    if nyo == "1":
        armory()
    if nyo == "2":
        capk()
    else:
        lol()

def hall():

    print("You appear in a room in another part of the space station.")
    print("Ulfric must have teleported you here.")
    print(" ")
    print("There is a table with a pen on it in the room.")
    print("You examine it, and see that it is gold with the words 'Space Dragon' written in glitter.")
    print(" ")
    print("That was easy enough. You leave the room to find the other two items.")
    print(" ")
    print("You are now in a hallway with two doors.")
    print("1. Left door")
    print("2. Right door")
    lol()

def nowwhat():
    global say
    if say == "1":
        print("Ulfric says:")
        print(" ")
        print("Yes, actually. The space station does have a sort of...")
        print("Alien problem. They tend to eat human flesh, so be careful. BYE!")
        print(" ")
        hall()
    if say == "2":
        print("Ulfric says:")
        print(" ")
        print("Yes GLITTER. I have something called STYLE. Get ROASTED.")
        print(" ")
        print("Ulfric ROASTS you.")
        dead()
    if say == "3":
        print("Ulfric says:")
        print(" ")
        print("You wont help me? Fine then. Get ROASTED!")
        print(" ")
        print("You have gotten ROASTED by Ulfric.")
    else:
        print("Please select an option.")
        nowwhat()

def yesulf():
    global say
    print(" ")
    print("Say:")
    print(" ")
    print("1. 'Sounds good. Anything else I should know?'")
    print("2. 'Glitter? Really, dude?'")
    print("3. 'That will take forever! I'm not helping you!' ")
    say = input(" ")
    nowwhat()

def bunks():
    global suit
    global bunk
    bunk = 1
    print("The only thing interesting in here is a space suit.")
    suit = input("Would you like to put it on?")
    print(" ")
    if suit == "yes":
        print("You put on the spacesuit and leave the room.")
        print(" ")
        suit = 1
        room()
    else:
        print("You leave the room without putting on the suit.")
        print(" ")
        room()

def tables():
    global tab
    tab = 1
    global cream
    print(" ")
    print("You examine the tables now. There are 12 packages of astronaut ice cream on the tables!")
    print(" ")
    if suit == 1:
        print("Because you are wearing the spacesuit, you can hold the ice cream in it!")
        cream = input("Do you want to take it with you?")
        if cream == "yes":
            print(" ")
            print("You hold the ice cream in your suit and leave the area.")
            cream = 1
        else:
            print(" ")
            print("You leave without taking the ice cream.")
    else:
        print(" ")
        print("You have no place to hold the ice cream, so you leave.")
        cream = 0
    if fri == 0:
        fridge()
    else:
        room()

def fridge():
    global fri
    fri = 1
    global dog

    print(" ")
    print("You walk over to the refrigerator. You see a german shepherd puppy checking out the food.")
    dog = input("The puppy is really cute. Do you want to see if she'll tag along with you?")
    if dog == "yes":
        print(" ")
        print("You pet the dog and she seems to be happy to be with you. You leave the area.")
        dog = 1
    else:
        print(" ")
        print("You ignore the dog and leave the area.")
    if tab == 0:
        tables()
    else:
        room()

def cafes():
    global cafe
    global fri
    fri = 0
    global tab
    tab = 0
    cafe = 1
    print("You enter the cafeteria.")
    print(" ")
    print(" Would you like to examine the...")
    print("1. Refrigerator")
    print("Or")
    nerp = input("2. Tables")

    if nerp == "1":
        fridge()
    elif nerp == "2":
        tables()
    else:
        print(" ")
        print("Please select an option.")
        print(" ")
        cafes()

def dead():
    ded = input("You have died. Press any key to start over.")
    spacedoor()

def action():
    global act
    print("Choose an action:")
    print(" ")
    print("1. 'I'm not helping you. Fight me.'")
    print("2. Shoot dragon with your laser gun")
    print("3. 'If you will send me home, I will help you.' ")
    if dog == 1 and cream == 1:
        print("4. Feed your dog some ice cream and ignore dragon.")
    act = input(" ")

    if act == "1":
        print("Ulfric says:")
        print("'Fight you? FIGHT YOU? I will ROAST you!'")
        print(" ")
        print("Ulfric gets up and ROASTS you with his fire breath.")
        dead()
    if act == "2":
        print("You attempt to shoot Ulfric, but you miss.")
        print("Ulfric says:")
        print(" ")
        print("'Get ROASTED!")
        print(" ")
        print("You have been roasted and killed.")
        dead()
    if act == "3":
        print("Ulfric says:")
        print("'Alright comrade, here is what I need you to do.")
        print(" ")
        print("I need you to retrieve three objects for me.")
        print("They are all gold, and say 'Space Dragon' on them in glitter.")
        print("They are scattered around the space station.")
        yesulf()
    if act == "4":
        print("Ulfric is angry that you would give your dog ice cream and not him.")
        print(" ")
        print("He ROASTS you for your rudeness.")
        dead()
    else:
        print("Please pick an option.")

def control():
    global act
    global dog
    global cream
    global cont
    cont = 1
    global bunk
    bunk = 1
    global cafe
    cafe = 1
    print("You enter the control room of the space station.")
    print(name, "is very surprised. There is a dragon sitting quietly in a chair.")
    print(" ")
    print(name, "says:")
    print(" ")
    print("'Who are you? Why is there a dragon in space?")
    print("Also, why am I a 28 year old Russian male?'")
    print("I am supposed to be a penguin!")
    print(" ")
    print("The dragon says:")
    print(" ")
    print("'My name is Ulfric The Space Dragon!")
    print("To answer your question, I am a dragon because it is cool.")
    print("You are a 28 year old Russian male because I used magic to turn you into one.")
    print("I have summoned you because I need your help.'")
    print(" ")
    action()

def room():
    print(" ")
    if bunk == 0:
        print("1. Dorm Area")

    if cafe == 0:
        print("2. Cafeteria")

    if cont == 0:
        print("3. Control Room")

    roomNum = input("Where would you like to go?")
    print(" ")
    if roomNum == "1" and bunk == 0:
        bunks()
    if roomNum == "2" and cafe == 0:
        cafes()
    if roomNum == "3" and cont == 0:
        control()
    else:
        print("Please pick a room you haven't visited before.")
        room()

def spacedoor():
    global bunk
    global cafe
    global cont
    global dog
    global cream
    global suit
    global cap
    global arb

    bunk = 0
    cafe = 0
    cont = 0
    dog = 0
    suit = 0
    cream = 0
    cap = 0
    arb = 0
    print("Your phone has disappeared, and you seem to be in space. The penguin now appears to be a 28 year old Russian "
        "male. That's odd.")

    print(" ")
    print(name, "says: 'What the hack? Where is my phone? Am I in space or something? "
                "And why am I a 28 year old Russian male? I used to be a penguin!")
    print(name, "finds that they have a laser pistol in a holster on their hip. I wonder what they need that for.")
    print(name, "says: 'I should probably look around for a way to get back home before I'm late for work.")
    print(" ")
    print("(When making decisions, press the number corresponding to the choice you want to make.)")
    print("(When making yes or no decisions, type 'yes' or 'no')")
    room()

spacedoor()
