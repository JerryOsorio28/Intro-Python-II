from room import Room
from player import Player
from items import Items

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

print('rooms', room.keys())

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Items
items = {
    'torch': Items('torch'),
    'shield': Items('shield'),
    'sword': Items('sword'),
    'coin': Items('coin')
}

#Places items in rooms
room['foyer'].items.append(str(items['torch']))
room['overlook'].items.append(items['shield'])
room['narrow'].items.append(items['sword'])
room['treasure'].items.append(items['coin'])

# if room:
#     print(True)
# else:
#     print(False)

# Make a new player object that is currently in the 'outside' room.
player_1 = Player('Jerry', room['outside'])

# Write a loop that:
game_on = True

name = input('Welcome Traveler! Tell me, what is your name? ')
text = input(f'{name}, are you ready for a great yet mysterious adventure? (yes/no) ')
print(f'Good luck traveler... You are currently {player_1.current_room}')

while game_on:
    print('player location**', player_1.current_room.name)
    print('player inventory', player_1.inventory)
    respond = input('Where would you like to go now? (You can move by typing n, s, w, e) ')
    if(text == 'yes'):
        if(respond == 'n'):
            if(player_1.current_room.n_to != None):
                player_1.current_room = player_1.current_room.n_to
                print(f'You have enter The {player_1.current_room}')
            else:
                print('There is nowhere to go that way!')
        if(respond == 's'):
            if(player_1.current_room.s_to != None):
                player_1.current_room = player_1.current_room.s_to
                print(f' You are currently at {player_1.current_room}')
            else:
                print('There is nowhere to go that way!')
        if(respond == 'w'):
            if(player_1.current_room.w_to != None):
                player_1.current_room = player_1.current_room.w_to
                print(f' You are currently at {player_1.current_room}')
            else:
                print('There is nowhere to go that way!')
        if(respond == 'e'):
            if(player_1.current_room.e_to != None):
                player_1.current_room = player_1.current_room.e_to
                print(f' You are currently at {player_1.current_room}')
            else:
                print('There is nowhere to go that way!')
        if(respond == 'search'):
            if(player_1.current_room.items):
                respond = input(f'There is a {player_1.current_room.items}, would you like to pick it up? (grab {player_1.current_room.items}, no) ')
                split_respond = respond.split(' ')
                if(split_respond[0] == 'grab'):
                    if(player_1.current_room.items.count(split_respond[1])):
                        # pass
                        player_1.inventory.append(split_respond[1])
                        items[split_respond[1]].on_take()
                        # room['foyer'].items.remove(split_respond[1])
                        player_1.current_room.items.remove(split_respond[1])
                        print('room items', player_1.current_room.items)
                    else:
                        print('if statement is not running')
                else:
                    print('You will not be able to see your way in the dark')
            else:
                print('There is nothing in this room')     
    elif(text == 'no'):
        print(f'I understand {name}, come back whenever you feel ready, goodbye.')
        game_on = False
    else:
        print('The value you typed is incorrect, choose one of the following: "yes" / "no"')

