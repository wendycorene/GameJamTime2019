#Functions

def listCommands():
    #list commands
    #check inventory, check num of remaining actions, examine item, take
    #   item, use item, examine room, move?,
    print("\t* EXAMINE")
    print("\t* USE")
    print("\t* GO")
    print("\t* TAKE")
    print("\t* TIME")
    print("\t* CANCEL")
    print("\t* INVENTORY")
    print()

def examine(room, descriptions, inventory):
    print("\tWhat would you like to examine?")
    print()
    whatToExamine = (input("\t\t>> ")).lower()
    print()
    if (room == "pod"):
        podCanExamine = ["note", "self", "pod"]
        if (whatToExamine in podCanExamine) and (whatToExamine in inventory):
            print("\t", descriptions.get(whatToExamine))
        else:
            print("\tI don't understand.")

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
        print("\tThere is nothing in your inventory.")
    else:
        print("\t+---------------+")
        print("\t|   INVENTORY   |")
        print("\t+---------------+")
        for item in inventory:
            print("\t   ",item)
    print()

def printActionsRemaining(dayActions):
    print("\t+------------------------+")
    print("\t|  ACTIONS REMAINING:", dayActions, " |")
    print("\t+------------------------+")
    print()

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


inventory = ["note"]
descriptions ={"note":"This is information about the note",
   "pod":"description of pod", "self":"description of self"}
gameComplete = False
currentRoom = "pod"
action = ""
printSplashScreen()
print()
while (gameComplete != True):
    dayActions = 5
    print("\tYou find yourself in a stasis pod...")
    print()
    while (dayActions!= 0):
        print("\tWhat would you like to do?")
        print()
        action = (input("\t\t>> ")).lower()
        print()
        if (action == "examine"):
            examine(currentRoom, descriptions, inventory)
            dayActions-= 1
            printActionsRemaining(dayActions)
        elif (action == "use"):
            print("USE")
            dayActions-= 1
            printActionsRemaining(dayActions)
        elif (action == "go"):
            print("GO")
            dayActions-= 1
            printActionsRemaining(dayActions)
        elif (action == "take"):
            print("TAKE")
            dayActions-= 1
            printActionsRemaining(dayActions)
        elif (action == "time"):
            printActionsRemaining(dayActions)
        elif (action == "cancel"):
            print("CANCEL")
            print()
        elif (action == "inventory"):
            printInventory(inventory)
        elif (action == "help"):
            listCommands()
        else:
            print("\tI don't understand. Try again or ask for HELP.")
            print()
    gameComplete = True
    print("you have reached the end of the game.")
input()
