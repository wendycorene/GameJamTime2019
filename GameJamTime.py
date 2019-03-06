#Functions

def listCommands():
    #list commands
    #check inventory, check num of remaining actions, examine item, take
    #   item, use item, examine room, move?,
    print()

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
        for item in inventory:
            print(item)

def printActionsRemaining(dayActions):
    print("\t============================")
    print("\t||  Actions remaining:", dayActions, " ||")
    print("\t============================")

def printSplashScreen():
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
    print()

inventory = []
gameComplete = False
printSplashScreen()
print("\tWhat is your name?")
print()
name = input("\t\t>> ")
print()
print("\tHello", name)
while (gameComplete!= True):
    dayActions = 5
    while (dayActions!= 0):
        printActionsRemaining(dayActions)
        dayActions-= 1
    gameComplete = True
input()
