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
    'torch': Items('Torch'),
    'sword': Items('Sword'),
    'shield': Items('Rusty Shield'),
    'sword': Items('Rusty Sword')
}



# Make a new player object that is currently in the 'outside' room.
player_1 = Player('James', room['outside'], [])

print(items[])


# Write a loop that:
# game_on = True

# name = input('Welcome Traveler! Tell me, what is your name? ')

# while game_on:
#     text = input(f'{name}, are you ready for a great yet mysterious adventure? (yes/no) ')

#     if(text == 'yes'):
#         print(f'Good luck traveler... You are currently {player_1.current_room}')
#         respond = input('Where would you like to go now? (You can move by typing n, s, w, e) ')
#         if(respond == 'n'):
#             if(player_1.current_room.n_to != None):
#                 player_1.current_room = player_1.current_room.n_to
#                 respond = input(f'We are finally in... The {player_1.current_room}, It is dark.. but there is a lit torch in the wall, would you like to grab it? (yes / no) ')
#                 if(respond == 'yes'):
#                     pass
#                 elif(respond == 'no'):
#                     print("You won't be able to see anything as you explore the cave")
#                 else:
#                     print('The value you typed is incorrect, choose one of the following: "yes" / "no" ')
#             else:
#                 print('There is nowhere to go that way!')
#         if(respond == 's'):
#             pass
#         if(respond == 'w'):
#             pass
#         if(respond == 'e'):
#             pass
        
#     elif(text == 'no'):
#         print(f'I understand {name}, come back whenever you feel ready, goodbye.')
#         game_on = False
#     else:
#         print('The value you typed is incorrect, choose one of the following: "yes" / "no"')

