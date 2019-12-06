from room import Room # Declare all the rooms
from player import Player
from item import Item

# player_name = input('Welcome! Please enter your name ') #<-- Where player initially inputs their name

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

#Make a new instance of Item
items = {
    'potion': Item('Potion Vial', 'Increases health'),
    'mana': Item('Mana Bottle', 'Increases mana'),
    'sword': Item('Sword', 'Rusty sword'),
    'shield': Item('Shield', 'Rusty shield')
}

# potion = Item('Potion Vial', 'Increases health')
potion = Item(items['potion'].name, items['potion'].description)
mana = Item(items['mana'].name, items['mana'].description)
sword = Item(items['sword'].name, items['sword'].description)
shield = Item(items['shield'].name, items['shield'].description)
room['foyer'].list.append(potion)
# print(potion)
    

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_1 = Player('Jerry', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

loop = False #Prevents an infinite loop

while not loop:
    print('PLAYER LOCATION', f"{player_1.current_room.name}")
    # print('PLAYER LOCATION', f"{'NORTH TO', player_1.current_room.n_to, 'SOUTH TO', player_1.current_room.s_to, 'EAST TO', player_1.current_room.e_to, 'WEST TO', player_1.current_room.w_to}")

    #Shows commands available for player
    #User has 4 options, 'n', 's', 'e', 'w' to move the player North, South, East or West.
    print("COMMANDS: 'n': North, 'e': East, 'w': West, 's': South, 'location': Current location, 'search': Search room")
    print('FOYER ROOM ITEM LIST', room['foyer'].list)
    print('PLAYER INVENTORY', player_1.inventory)

    # print('ARRAY', room['foyer'].list)

    #Ask the user what he/she would like to do next
    option = input("Where would you like to go ")

    if option == 'search':
            if player_1.current_room.name == 'Foyer':
                answer = input(f'Searching the room you found a {potion.name}, would you like to take it? ')
                answer= answer.split()
                for words in answer:
                    if len(answer) > 1:
                        if answer[0] == 'take':
                            if answer[1] == 'potion':
                                for item in room['foyer'].list:
                                    # print('ITS WORKING***', item.name)
                                    if item.name == 'Potion Vial':
                                        room['foyer'].list.remove(item)
                                        player_1.inventory.append(item)
                                        print(f'You have picked the {potion}')

                
    else:
    #Checks if player is able to move to an existing room, if there's an existing room, moves player to North, else display's message.
        if option == 'n':
            print(player_1.current_room.n_to)
            if player_1.current_room.n_to is None:
                print("You cant go that way!")
                player_1.current_room
            else:
                player_1.current_room = player_1.current_room.n_to

        #Checks if player is able to move to an existing room, if there's an existing room, moves player to South, else display's message.
        elif option == 's':
            print(player_1.current_room.s_to)
            if player_1.current_room.s_to is None:
                print("You cant go that way!")
                player_1.current_room
            else:
                player_1.current_room = player_1.current_room.s_to

        #Checks if player is able to move to an existing room, if there's an existing room, moves player to East, else display's message.
        elif option == 'e':
            print(player_1.current_room.e_to)
            if player_1.current_room.e_to is None:
                print("You cant go that way!")
                player_1.current_room
            else:
                player_1.current_room = player_1.current_room.e_to

        #Checks if player is able to move to an existing room, if there's an existing room, moves player to West, else display's message.
        elif option == 'w':
            print(player_1.current_room.w_to)
            if player_1.current_room.w_to is None:
                print("You cant go that way!")
                player_1.current_room
            else:
                player_1.current_room = player_1.current_room.w_to

        #Prints player's current location
        elif option == 'location':
            print(f'Your current location is {player_1.current_room}')

        #Prints an error of players types an invalid character(s)
        # elif len(option) > 1 and option != 'location' and option != 'search':
        #     print('Invalid characters! Choose n/s/w/e to move your player.')
        
            # elif player_1.current_room.name == 'Foyer':
            #     print(f'Searching the room, you found  {player_1.current_room.name}')

        if option == 'q':
            print('Thanks for playing, goodbye!')
            break

        

    
