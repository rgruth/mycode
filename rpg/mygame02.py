#!/usr/bin/python3
'''My RPG Game in my NAPYA Class'''

def showInstructions():
    print('''
    RPG Game
    Your task is to escape the houser with the key and the potion
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
            'east' : 'Dining Room',
            'item' : 'key'
            },
        'Kitchen' : {
            'north' : 'Hall'
            'item' : 'monster'
            },
        'Dining Room' : {
            'west' : 'Hall'
            'item' : 'potion'
            },
        'Garden' : {
            'north' : 'Dining Room'
            },
        'Pantry' : {
            'south' : 'Dining Room',
            'item' : 'cookie'
            },
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
        else: 
            print('YOU CANNOT GET ', move[1], '!')

    # gonna get eaten by a monster in the kitchen!
    if 'item' in rooms[currentRoom] and 'monster' in room[currentRoom]['item']:
        print('A monster has got you! GAME OVER!')
        break # excape the loop

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print("You escaped the house with the ultra rare key and the magic potion... YOU WIN!)
