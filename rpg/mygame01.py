#!/usr/bin/python3
'''My RPG Game in my NAPYA Class'''

def showInstructions():
    print('''
    RPG Game
    --------
    Commands:
        go [direction]
        get [item]
    ''')

def showStatus(): # display the player's status
    print('=================')
    print('You are in the ', currentRoom)
    # show inventory
    print('Inventory : ', str(inventory))
    if 'item' in rooms[currentRoom]:
        print('You see a ', rooms[currentRoom]['item'])
    print('=================')

# init a empty list
inventory = []

# create our world and its rooms
rooms = {
        'Hall' : {
            'south' : 'Kitchen',
            'item' : 'key'
            },
        'Kitchen' : {
            'north' : 'Hall'
            }
        }

# player start location
currentRoom = 'Hall'

# show instructions to the player
showInstructions()

# create an infinite loop
while True:
    showStatus()
    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split() #make everything lower case because directions and items require it, then split into a list

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]: 
            currentRoom = rooms[currentRoom][move[1]]
            # if YES that direction exists, then assign your new current room to the value of the key the user entered
        else: 
            print("YOU CAN'T GO THAT WAY!")

    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]] # add item to inventory
            print(move[1] + ' got!')# msg saying you recieved the item
            del rooms[currentRoom]['item'] # deletes that item from the dictionary

