from room import Room # Declare all the rooms
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_1 = Player('Jerry', room['outside'])
print(player_1)

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
    print('CURRENT PLAYER LOCATION', f"{player_1.current_room.name}")

    #Ask the user what he/she would like to do next
    option = input("If you are ready, press n to head north into the cave ")

    #User has 4 options, 'n', 's', 'e', 'w' to move the player North, South, East or West.
    
    #Checks if player is able to move to an existing room, if there's an existing room, moves player to North, else display's message.
    if option == 'n':
        if player_1.current_room.n_to == None:
            print("You cant go that way!")
            player_1.current_room
        else:
            player_1.current_room = player_1.current_room.n_to

     #Checks if player is able to move to an existing room, if there's an existing room, moves player to South, else display's message.
    elif option == 's':
        if player_1.current_room.s_to == None:
            print("You cant go that way!")
            player_1.current_room
        else:
            player_1.current_room = player_1.current_room.s_to

     #Checks if player is able to move to an existing room, if there's an existing room, moves player to East, else display's message.
    elif option == 'e':
        if player_1.current_room.e_to == None:
            print("You cant go that way!")
            player_1.current_room
        else:
            player_1.current_room = player_1.current_room.e_to

    #Checks if player is able to move to an existing room, if there's an existing room, moves player to West, else display's message.
    elif option == 'w':
        if player_1.current_room.w_to == None:
            print("You cant go that way!")
            player_1.current_room
        else:
            player_1.current_room = player_1.current_room.w_to

    if option == 'q':
        print('Thanks for playing, goodbye!')
        break


    

        

    
