#Global Variable
terminalLocked = True
eatenByGrue = False
gasLeaking = True
systemFlushed = False
gameComplete = False

#Functions

def listCommands():
    #list commands
    #check inventory, check num of remaining actions, examine item, take
    #   item, use item, examine room, move?,
    print()
    print("\tPOSSIBLE ACTIONS: EXAMINE, USE, GO, TAKE, TIME, INVENTORY")
    print()

def use(currentRoom, inventory, descriptions, roomsContain):
    global terminalLocked
    global eatenByGrue
    global gasLeaking
    thingsInRoom = roomsContain.get(currentRoom)
    print()
    print("\tWHAT WOULD YOU LIKE TO USE?")
    print()
    whatToUse = (input("\t\t>> ")).lower()
    if (whatToUse == "terminal" and currentRoom == "engineering" and terminalLocked == False):
        useTerminal()
    elif (whatToUse == "logs" and currentRoom == "bridge"):
        print()
        print("logs")
    elif (whatToUse == "button" and currentRoom == "pod"):
        print()
        print("\tThe stasis CHAMBER is in front of you.")
    elif (whatToUse in inventory):
        if (currentRoom == "captain quarters" and (whatToUse == "crowbar" or whatToUse == "mop")):
            print()
            updateCapQuartDict(descriptions)
            print("\t" + descriptions.get("captain quarters"))
            removeFromInventory(whatToUse, inventory)
        if (currentRoom == "engineering" and whatToUse == "keycard" and terminalLocked == True):
            print()
            print("\tTERMINAL UNLOCKED")
            terminalLocked = False
            removeFromInventory(whatToUse, inventory)
        if (currentRoom == "maintenance" and whatToUse == "wrench"):
            print()
            print("\tYou manage to use the wrench to turn the valve. The gas leak has stopped, but there is still gas in the air.")
            removeFromInventory(whatToUse, inventory)
            gasLeaking = False
        if (currentRoom == "mess" and whatToUse == "bolt cutters"):
            print()
            descriptions["cabinet"] = "You break through the padlock and open the cabinet to find a tea set."
            print("\t" + descriptions.get("cabinet"))
            removeFromInventory(whatToUse, inventory)
        if (whatToUse == "tea set"):
            print()
            print("YOU ARE EATEN BY A GRUE.")
            eatenByGrue = True
            removeFromInventory(whatToUse, inventory)
    else:
        print()
        print("\tYOU DON'T HAVE THAT ITEM.")

def take(descriptions, inventory, currentRoom, roomsContain):
        thingsInRoom = roomsContain.get(currentRoom)
        print()
        print("\tWHAT WOULD YOU LIKE TO TAKE?")
        print()
        whatToTake = (input("\t\t>> ")).lower()
        if (whatToTake in thingsInRoom):
            inventory.append(whatToTake)
            thingsInRoom.remove(whatToTake)
            roomsContain[currentRoom] = thingsInRoom
            printInventory(inventory)
        else:
            print("\tI DON'T UNDERSTAND.")

def examine(currentRoom, descriptions, inventory, roomsContain):
    thingsInRoom = roomsContain.get(currentRoom)
    print()
    print("\tWHAT WOULD YOU LIKE TO EXAMINE?")
    print()
    whatToExamine = (input("\t\t>> ")).lower()
    print()
    if (whatToExamine == "room"):
        print("\t" + descriptions.get(currentRoom))
    elif (whatToExamine == "button" and currentRoom == "pod"):
        print("\t" + descriptions.get(whatToExamine))
    elif (whatToExamine in thingsInRoom or whatToExamine in inventory):
        print("\t" + descriptions.get(whatToExamine))
    else:
        print("\tI DON'T UNDERSTAND.")

def checkInventory(item, inventory):
    #check to see if something is in the inventory
    inInventory = False
    if item in inventory:
        inInventory = True
    return inInventory

def removeFromInventory(item, inventory):
    #remove an item from inventory
    if item in inventory:
        inventory.remove(item)

def printInventory(inventory):
    #prints the inventory
    if (len(inventory) == 0):
        print()
        print("\tTHERE IS NOTHING IN YOUR INVENTORY.")
    else:
        print()
        print("\t+---------------+")
        print("\t|   INVENTORY   |")
        print("\t+---------------+")
        for item in inventory:
            print("\t   ",item)
    print()

def printActionsRemaining(dayActions):
    print()
    print("\t+------------------------+")
    print("\t|  ACTIONS REMAINING:", dayActions, " |")
    print("\t+------------------------+")
    print()

def updatePodsDict(dictionary, key, value):
    newDef = "As you exit the pod, you see the familiar interior of your spacecraft. As the metallic walls come into focus,\n\tyou notice " + str(value) + " other pods around you, lining the walls of the room. No one else has woken up."
    dictionary[key] = newDef

def goTo(allRooms, currentRoom):
    print()
    print("\tWHERE WOULD YOU LIKE TO GO?")
    print()
    whereToGo = (input("\t\t>> ")).lower()
    if (whereToGo == currentRoom):
        print()
        print("\tYOU'RE ALREADY THERE.")
        print()
        return currentRoom
    elif (whereToGo in allRooms):
        return whereToGo
    else:
        print()
        print("\tI DON'T UNDERSTAND.")
        print()
        return currentRoom

def updateCapQuartDict(dictionary):
    newDef = "After prying the door open, you slowly enter the Captain’s Quarters.\n\tYou go straight over to the Captain’s desk, delicately pawing through the things cluttering their desk.\n\tYou go through the drawers of the cluttered desk and find a book titled, \"Captain’s Manual\"."
    dictionary["captain quarters"] = newDef

def useTerminal():
    global gameComplete
    choice = " "
    while (choice != "quit"):
        print("\tThe screen is garbled. You can make out the following:")
        print("\tSCAN ship .... sensors..... ")
        print("\tAccess .... MAP")
        print("\tFLUSH ..... pipes.... oxygen....")
        print("\t...QUIT....")
        print()
        print("\tINPUT:")
        print()
        choice = (input("\t\t>> ")).lower()
        print()
        if (choice == "scan"):
            print("\t...leak...poison...Maintenance Closet.")
        elif (choice == "map"):
            print("\tThe map is difficult to read,",
            "but you can make out the following ship locations:\n",
            "\t\tCHAMBER \tBRIDGE \t\tENGINEERING\n",
            "\t\tMAINTENANCE \tMESS \t\tCAPTAIN QUARTERS")
            print()
        elif (choice == "flush"):
            print("\t To FLUSH.... oxygen.... password:")
            print()
            print("\tINPUT:")
            print()
            password = (input("\t\t>> ")).lower()
            if (password == "fhqwhgads" and gasLeaking == True):
                print("\tPassword correct.")
                print("\tDangerous particles still detected.")
            if (password == "fhqwhgads" and gasLeaking == False):
                print("\tPassword correct.")
                print("\tAir Supply Decontaminated.")
                gameComplete = True
                break
            else:
                print("\tPassword incorrect.")

        elif (choice == "quit"):
            print("\tThe terminal flickers to black.")
            print()
            break
        else:
            print("\tInvalid input.")


"""def printSplashScreen():
    print()
    print("\t             O")
    print("\t            (_)")
    print("\t          _ )_( _")
    print("\t        /`_) H (_`\\")
    print("\t      .' (  { }  ) '.")
    print("\t    _/ /` '-'='-' `\\ \\_       __  __             _          ")
    print("\t   [_.'   _,...,_   '._]     |  \\/  | __ _ _   _| |__   ___ ")
    print("\t    |   .:\"`````\":.   |      | |\\/| |/ _` | | | | '_ \\ / _ \\")
    print("\t    |__//_________\\\\__|      | |  | | (_| | |_| | |_) |  __/")
    print("\t     | .-----------. |       |_|  |_|\\__,_|\\__, |_.__/ \\___|")
    print("\t     | |  .-\"\"\"-.  | |                     |___/            ")
    print("\t     | | /    /  \\ | |")
    print("\t     | ||-   <   -|| |                  _   _           _   ")
    print("\t     | | \\    \\  / | |                 | \\ | | _____  _| |_")
    print("\t     | |[`'-...-'`]| |                 |  \\| |/ _ \\ \\/ / __|")
    print("\t     | | ;-.___.-; | |                 | |\\  |  __/>  <| |_ ")
    print("\t     | | |  |||  | | |                 |_| \\_|\___/_/\\_\\\\__|")
    print("\t     | | |  |||  | | |")
    print("\t     | | |  |||  | | |")
    print("\t     | | |  |||  | | |               _____ _                ")
    print("\t     | | |  |||  | | |              |_   _(_)_ __ ___   ___ ")
    print("\t     | | | _|||_ | | |                | | | | '_ ` _ \\ / _ \\")
    print("\t     | | | >===< | | |                | | | | | | | | |  __/")
    print("\t     | | | |___| | | |                |_| |_|_| |_| |_|\\___|")
    print("\t     | | |  |||  | | |")
    print("\t     | | |  ;-;  | | |")
    print("\t     | | | (   ) | | |")
    print("\t     | | |  '-'  | | |         By: Hannah Jahal & Wendy King")
    print("\t     | | '-------' | |")
    print("\tjgs _| '-----------' |_")
    print("\t   [= === === ==== == =]")
    print("\t   [__--__--___--__--__]")
    print("\t  /__-___-___-___-___-__\\")
    print("\t `\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"`")
    print()
    print()"""

def printSplashScreen():
    print(" *   .      *  .        *       .       .       *    .       .             *")
    print("      *    .  *    __  __             _               .             *")
    print("                  |  \\/  | __ _ _   _| |__   ___        *")
    print(" *   .        *   | |\\/| |/ _` | | | | '_ \\ / _ \\    .       .       *")
    print("   .     *        | |  | | (_| | |_| | |_) |  __/")
    print("           .     .|_|  |_|\\__,_|\\__, |_.__/ \\___|  *        *")
    print("       .              .       . |___/      *      .")
    print("      *    .  *                         .                       *")
    print(".  *            *       _   _       *   _       *")
    print("                       | \\ | | _____  _| |_ .       *")
    print("         *         .   |  \\| |/ _ \\ \\/ / __|      *          .")
    print("      *    .   *       | |\\  |  __/>  <| |_      .    *")
    print("                   *   |_| \\_|\___/_/\\_\\\\__|   .      .")
    print("      *    .  *                               .             *")
    print(" *    .         .     _____ _          *        .       *")
    print("   .      *          |_   _(_)_ __ ___   ___      *       .    .     *")
    print("     .    .   *        | | | | '_ ` _ \\ / _ \\ *      .")
    print("    .            .     | | | | | | | | |  __/   .       *")
    print(".   *      *           |_| |_|_| |_| |_|\\___|       *    .")
    print("                          .              ")
    print("   *          .   *           .  *        *       ")
    print("         *          .   *      .     *        .  *        *       ")
    print(" *    .  *    *    .  *    By: Hannah Jahal & Wendy King   .      .             *")
    print(" *   .        *    *   .        *       .           .       *")


inventory = [""]
numberOfPods = 87
bodies = 0
descriptions = {"pod":"You slowly regain consciousness and as you open your eyes, you find yourself in one of the stasis pods.\n\tA voice repeatedly alerts you: \"Officer Vazquez to Engineering. Officer Vazquez to Engineering.\" \n\tThere is a button in front of you.",
                "chamber": "As you exit the pod, you see the familiar interior of your spacecraft. As the metallic walls come into focus,\n\tyou notice 87 other pods around you, lining the walls of the room. No one else has woken up.",
                "bridge": "You see the logs systems within the main console of the ship. Windows line the entirety of the\n\tnose of the ship, providing a seemingly endless view of the starry expanse.",
                "engineering": "You enter Engineering, a room that you’ve spent countless hours in since taking on the\n\tposition of Head Engineer. You look around at the familiar space, filled with terminals,\n\treactors and cargo containers. You go up your usual terminal. ",
                "maintenance": "You enter the maintenance closet, looking for anything of use.\n\tYou see a crowbar, a wrench, and bolt cutters.\n\tYou see a large pipe along the side of the wall with gas spewing out.",
                "mess": "You see tables and chairs strewn about the room with half-eaten plates of food\n\tthat seem to have been abandoned during the emergency alert. You see your keycard sitting on\n\tone of the tables and a locked cabinet and a mop in the corner.",
                "captain quarters": "You approach the door to the Captain’s Quarters, only to find that the door is jammed shut and will not open.",
                "wrench": "A tool used to provide grip. It’s also heavy enough to kill a man.",
                "crowbar": "An iron tool with a curved end, often used as a lever/to pry things open.",
                "mop": "This mop is worn out, but sturdy and capable.",
                "tea set": "This tea set is pale green with four tiny tea cups and various tea-like things.\n\tYou haven’t seen a tea set quite like this since visiting your grandmother years ago. ",
                "manual": "You thumb through the book slowly, looking for anything that could be of use.\n\tIf anyone knows about emergency protocols, it’s Captain Whitaker.\n\tThey’re the kind of captain who puts safety as our top priority.\n\tYou wonder if they had anything to do with the fact that you were the one programmed\n\tto wake up in case of an emergency like this.\n\tYou skim through a significant amount of text messily scrawled on the pages, but you eventually find\n\ta password labeled “Override Password”. The password reads: fhqwhgads.\n\tThis might be important.",
                "bolt cutters": "A tool used to cut through chains, padlocks, and all sorts of other sturdy looking things.",
                "keycard": "A worn keycard with your name on it. It reads: Officer Meg Velasquez.",
                "logs": "You hear alarms, followed by nervous chatter between crew members.\n\tThe audio becomes choppy, but you can make out the following:\n\t\"Captain! Asteroid... Incoming!\"\n\tThe dialogue is interrupted by explosions and screams.\n\t\"Teleport everyone... pods!... Prepare for impact... Oh God--It's--\"\n\tThe audio cuts off there. Upon impact with asteroid, the teleportation system must have sent everyone back\n\tto their pods. There has to be a way to wake everyone back up...",
                "cabinet": "The cabinet is padlocked shut, keeping it tightly guarded.",
                "door": "The metallic door is jammed shut and the card reader is offline.\n\tIt seems the only way to open this door is with a leveraging tool of some sort.",
                "pipe": "Upon further examination, you see a VERY large hole and a stuck valve.\n\tThere must be some way to redirect the gas.",
                "button": "The button says exit."}
roomsContain = {"pod": ["button", "pod"],
                "chamber": ["chamber"],
                "bridge": ["bridge", "logs"],
                "engineering": ["engineering", "terminal"],
                "maintenance": ["maintenance", "crowbar", "wrench", "bolt cutters", "pipe"],
                "mess": ["mess", "tea set", "mop", "keycard", "cabinet"],
                "captain quarters": ["captain quarters", "door", "manual"]}
allRooms = ["pod", "chamber", "engineering", "maintenance", "captain quarters",
            "mess", "bridge"]
action = ""
printSplashScreen()
print()
while (gameComplete != True):
    dayActions = 5
    eatenByGrue = False
    currentRoom = "pod"
    print("\t" + descriptions.get(currentRoom))
    print()
    while (dayActions!= 0):
        print("\tWHAT WOULD YOU LIKE TO DO?")
        print()
        action = (input("\t\t>> ")).lower()
        if (action == "examine"):
            examine(currentRoom, descriptions, inventory, roomsContain)
            dayActions-= 1
            printActionsRemaining(dayActions)
        elif (action == "use"):
            use(currentRoom, inventory, descriptions, roomsContain)
            dayActions-= 1
            if (eatenByGrue == True):
                dayActions = 0
            printActionsRemaining(dayActions)
        elif (action == "go"):
            previousRoom = currentRoom
            currentRoom = goTo(allRooms, currentRoom)
            if (previousRoom != currentRoom):
                dayActions-= 1
                printActionsRemaining(dayActions)
        elif (action == "take"):
            take(descriptions, inventory, currentRoom, roomsContain)
            dayActions-= 1
            printActionsRemaining(dayActions)
        elif (action == "time"):
            printActionsRemaining(dayActions)
        elif (action == "inventory"):
            printInventory(inventory)
        elif (action == "help"):
            listCommands()
        elif (action == "uuddlrlrbastart"):
            gameComplete = True
            break
        else:
            print()
            print("\tI DON'T UNDERSTAND. TRY AGAIN OR ASK FOR HELP.")
            print()
        if (gameComplete == True):
            break
    numberOfPods -= 1
    bodies += 1
    updatePodsDict(descriptions, "chamber", numberOfPods)

print()
print("\tA strong woosh surrounds you. Any alarms are calmed. You hear Captain Whitaker's voice in your ear:\n\t\"Velasquez! Meet me on the bridge!\"")
print("\tAs you make your way to the bridge, you see people slowly trickling out of the stasis chamber room.")
print("\tOn the bridge, Captain Whitaker thanks you for fixing the situation.")
print("\t\"Ensign, how many were lost?\"")
print("\t\"" + str(bodies) + ", Captain.\"")
print("\tUnfortunately, Meg, every time you were teleported back to your pod, an exorbitant amount of energy\n\twas needed to revive you. In the process, sacrifices were necessary in order to save everyone else on the ship.")
print("\tAs you look out the window, you see " + str(bodies) + " bodies floating lifelessly in space.")
print("\tMaybe next time...")
print()
input()
