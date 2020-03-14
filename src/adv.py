from room import Room
from player import Player
from items import Items, Potion
from enemies import Enemies

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", '''\n"North of you, the cave mount beckons"\n'''),

    'foyer':    Room("The Foyer", """\nDim light filters in from the south. Dusty passages run north and east.\n"""),

    'overlook': Room("Grand Overlook", """\nA steep cliff appears before you, falling into the darkness.\n Ahead to the north, a light flickers in the distance, but there is no way across the chasm.\n"""),

    'narrow':   Room("Narrow Passage", """\nThe narrow passage bends here from west to north. The smell of gold permeates the air.\n"""),

    'treasure': Room("Treasure Chamber", """\nYou've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.\n"""),
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

# Items in the game
items = {
    'torch': Items('torch', 0),
    'shield': Items('shield', 0),
    'sword': Items('sword', 20),
    'potion': Potion('potion', 30),
    'rock': Items('rock', 10),
    # 'coin': Items('coin')
}

#Places items in rooms
room['foyer'].items.append(str(items['sword']))
room['overlook'].items.append(str(items['shield']))
room['narrow'].items.append(str(items['torch']))
room['narrow'].items.append(str(items['potion']))
room['foyer'].items.append(str(items['rock']))
room['overlook'].items.append(str(items['rock']))
room['narrow'].items.append(str(items['rock']))
# room['treasure'].items.append(str(items['coin']))



# Enemies in the game
enemies = {
    'goblin_1': Enemies('goblin'),
    'goblin_2': Enemies('goblin'),
    'goblin_3': Enemies('goblin')
}

# Placing enemies in rooms
room['overlook'].enemies.append(enemies['goblin_1'])
room['narrow'].enemies.append(enemies['goblin_2'])
room['treasure'].enemies.append(enemies['goblin_3'])

# print('enemies in overlook', room['overlook'].enemies)

# Make a new player object that is currently in the 'outside' room.
player_1 = Player('Jerry', room['outside'])

# Write a loop that as long as it is True, the game will run, else quits the game
game_on = True

name = input('Welcome Traveler! Tell me, what is your name? ')
text = input(f'{name}... interesting. Well {name}! are you ready for a great yet mysterious adventure? (yes/no) ')
print(f'\n Good luck traveler... \n You are currently {player_1.current_room}')

while game_on:
    print("Type 'help' if you need assistance")
    respond = input('Where would you like to go now? ')
    if(text == 'yes'):
        if(respond == 'n'):
            # checks first if there is an existing room where the player wants to go
            if(player_1.current_room.n_to != None):
                # if there is the player is moved to the room on that direction
                player_1.current_room = player_1.current_room.n_to
                print(f'\nYou have enter {player_1.current_room}')
                # check if there is any enemies in the current room
                if(len(player_1.current_room.enemies) > 0):
                    for enemy in player_1.current_room.enemies:
                        print(f'\nWatch out! You have encounter a {enemy.name} Attack if you have a weapon, if not, is best to retreat!\n')
                        # this check as long as the enemy is still alive
                        while (enemy.dead == False):
                            respond = input('\nWhat do you want to do? (attack / retreat)\n ')
                            # if player decided to attack, it will calculate the damage done to the enemy by subtracting the player's current attack power from the health of the enemy
                            if(respond == 'attack'):
                                enemy.health = enemy.health - player_1.attack
                                if(enemy.health > 0):
                                    player_1.health = player_1.health - enemy.attack
                                    print(f'\nYou have attacked the {enemy.name}, dealing {player_1.attack} of damage, enemy health: {enemy.health}\n')
                                    # checks if the health of player has not fully deplete yet, if it did, it's game over.
                                    if(player_1.health <= 0):
                                        print(f'\nEnemy has attacked, dealing {enemy.attack} damage, your health now is {player_1.health}\n')
                                        print(f'\nThe {enemy.name} has killed you, game over.\n')
                                        game_on = False
                                        break
                                    else:
                                        print(f'\nEnemy has attacked, dealing {enemy.attack} damage, your health now is {player_1.health}\n')
                                else:
                                    print(f'\nYou have killed the {enemy.name}.. It seems you are not in any danger... for now.\n')
                                    # removes the enemy from the room
                                    player_1.current_room.enemies.remove(enemy)
                                    # breaks out of the while loop
                                    enemy.dead = True
                            # if the player decides to retreat, it will take it back to the previous room and break the while loop
                            elif(respond == 'retreat'):
                                player_1.current_room = player_1.current_room.s_to
                                print('\nYou have escaped... for now.\n')
                                break

            else:
                print('\nYou cannot go that way!\n')
        if(respond == 's'):
            if(player_1.current_room.s_to != None):
                player_1.current_room = player_1.current_room.s_to
                print(f'\nYou are currently at {player_1.current_room}\n')
                # check if there is any enemies in the current room
                if(len(player_1.current_room.enemies) > 0):
                    for enemy in player_1.current_room.enemies:
                        print(f'\nWatch out! You have encounter a {enemy.name} Attack if you have a weapon, if not, is best to retreat!\n')
                        # this check as long as the enemy is still alive
                        while (enemy.dead == False):
                            respond = input('\nWhat do you want to do? (attack / retreat)\n ')
                            # if player decided to attack, it will calculate the damage done to the enemy by subtracting the player's current attack power from the health of the enemy
                            if(respond == 'attack'):
                                enemy.health = enemy.health - player_1.attack
                                if(enemy.health > 0):
                                    player_1.health = player_1.health - enemy.attack
                                    print(f'\nYou have attacked the {enemy.name}, dealing {player_1.attack} of damage, enemy health: {enemy.health}\n')
                                    # checks if the health of player has not fully deplete yet, if it did, it's game over.
                                    if(player_1.health <= 0):
                                        print(f'\nEnemy has attacked, dealing {enemy.attack} damage, your health now is {player_1.health}\n')
                                        print(f'\nThe {enemy.name} has killed you, game over.\n')
                                        game_on = False
                                        break
                                    else:
                                        print(f'\nEnemy has attacked, dealing {enemy.attack} damage, your health now is {player_1.health}\n')
                                else:
                                    print(f'\nYou have killed the {enemy.name}.. It seems you are not in any danger... for now.\n')
                                    # removes the enemy from the room
                                    player_1.current_room.enemies.remove(enemy)
                                    # breaks out of the while loop
                                    enemy.dead = True
                            # if the player decides to retreat, it will take it back to the previous room and break the while loop
                            elif(respond == 'retreat'):
                                player_1.current_room = player_1.current_room.s_to
                                print('\nYou have escaped... for now.\n')
                                break
            else:
                print('\nYou cannot go that way!\n')
        if(respond == 'w'):
            if(player_1.current_room.w_to != None):
                player_1.current_room = player_1.current_room.w_to
                print(f'\nYou are currently at {player_1.current_room}\n')
                # check if there is any enemies in the current room
                if(len(player_1.current_room.enemies) > 0):
                    for enemy in player_1.current_room.enemies:
                        print(f'\nWatch out! You have encounter a {enemy.name} Attack if you have a weapon, if not, is best to retreat!\n')
                        # this check as long as the enemy is still alive
                        while (enemy.dead == False):
                            respond = input('\nWhat do you want to do? (attack / retreat)\n ')
                            # if player decided to attack, it will calculate the damage done to the enemy by subtracting the player's current attack power from the health of the enemy
                            if(respond == 'attack'):
                                enemy.health = enemy.health - player_1.attack
                                if(enemy.health > 0):
                                    player_1.health = player_1.health - enemy.attack
                                    print(f'\nYou have attacked the {enemy.name}, dealing {player_1.attack} of damage, enemy health: {enemy.health}\n')
                                    # checks if the health of player has not fully deplete yet, if it did, it's game over.
                                    if(player_1.health <= 0):
                                        print(f'\nEnemy has attacked, dealing {enemy.attack} damage, your health now is {player_1.health}\n')
                                        print(f'\nThe {enemy.name} has killed you, game over.\n')
                                        game_on = False
                                        break
                                    else:
                                        print(f'\nEnemy has attacked, dealing {enemy.attack} damage, your health now is {player_1.health}\n')
                                else:
                                    print(f'\nYou have killed the {enemy.name}.. It seems you are not in any danger... for now.\n')
                                    # removes the enemy from the room
                                    player_1.current_room.enemies.remove(enemy)
                                    # breaks out of the while loop
                                    enemy.dead = True
                            # if the player decides to retreat, it will take it back to the previous room and break the while loop
                            elif(respond == 'retreat'):
                                player_1.current_room = player_1.current_room.s_to
                                print('\nYou have escaped... for now.\n')
                                break
            else:
                print('\nYou cannot go that way!\n')
        if(respond == 'e'):
            if(player_1.current_room.e_to != None):
                player_1.current_room = player_1.current_room.e_to
                print(f' You are currently at {player_1.current_room}')
                # check if there is any enemies in the current room
                if(len(player_1.current_room.enemies) > 0):
                    for enemy in player_1.current_room.enemies:
                        print(f'\nWatch out! You have encounter a {enemy.name} Attack if you have a weapon, if not, is best to retreat!\n')
                        # this check as long as the enemy is still alive
                        while (enemy.dead == False):
                            respond = input('\nWhat do you want to do? (attack / retreat)\n ')
                            # if player decided to attack, it will calculate the damage done to the enemy by subtracting the player's current attack power from the health of the enemy
                            if(respond == 'attack'):
                                enemy.health = enemy.health - player_1.attack
                                if(enemy.health > 0):
                                    player_1.health = player_1.health - enemy.attack
                                    print(f'\nYou have attacked the {enemy.name}, dealing {player_1.attack} of damage, enemy health: {enemy.health}\n')
                                    # checks if the health of player has not fully deplete yet, if it did, it's game over.
                                    if(player_1.health <= 0):
                                        print(f'\nEnemy has attacked, dealing {enemy.attack} damage, your health now is {player_1.health}')
                                        print(f'The {enemy.name} has killed you, game over.')
                                        game_on = False
                                        break
                                    else:
                                        print(f'\nEnemy has attacked, dealing {enemy.attack} damage, your health now is {player_1.health}\n')
                                else:
                                    print(f'\nYou have killed the {enemy.name}.. It seems you are not in any danger... for now.\n')
                                    # removes the enemy from the room
                                    player_1.current_room.enemies.remove(enemy)
                                    # breaks out of the while loop
                                    enemy.dead = True
                            # if the player decides to retreat, it will take it back to the previous room and break the while loop
                            elif(respond == 'retreat'):
                                player_1.current_room = player_1.current_room.s_to
                                print('You have escaped... for now.')
                                break
            else:
                print('\nYou cannot go that way!\n')
        if(respond == 'search'):
            # when searching for items, it checks if there is any items in the room first
            if(player_1.current_room.items):
                # if there is, prompts the player what he wants to do with it
                respond = input(f'\nSearching the room, You have found a {player_1.current_room.items}, would you like to pick it up? (grab {player_1.current_room.items} / no)\n ')
                # for two or more words, it splits the string
                split_respond = respond.split(' ')
                if(split_respond[0] == 'grab'):
                    # it checks if there is such item in the room first
                    if(player_1.current_room.items.count(split_respond[1])):
                        # if there is, adds item to player inventory
                        player_1.inventory.append(split_respond[1])
                        # increases player's attack when picking up sword
                        if(split_respond[1] == 'sword'):
                            # runs the method to display which items was picked up.
                            items[split_respond[1]].on_take()
                            player_1.attack += items[split_respond[1]].attack
                            print(f'Your attack power increased by {items[split_respond[1]].attack}')
                        elif(split_respond[1] == 'potion'):
                            player_1.health += items[split_respond[1]].health 
                            print(f"You've recover {items[split_respond[1]].health} points of your health.")

##IN THE FUTURE, MORE ADVANCE FEATURES LIKE ARMOR, SHIELD, HELMET, MANA.. WHEN PICKED UP, THE EFFECT THAT HAS ON THE CHARACTER CAN BE ADDED HERE##

                        # removes item from the room
                        player_1.current_room.items.remove(split_respond[1])
                # elif(split_respond[0] == 'no'):
                #     print('It will be very difficult to see your way in the dark...')
                else:
                    print('The value you typed is incorrect')
            else:
                print('There is nothing in this room')
        # if the player types drop, it will be prompted what item he wants to drop from inventory 
        elif(respond == 'drop'):
            respond = input(f'What item would you like to drop? {player_1.inventory} ' )
            # check if response is in his inventory
            if(player_1.inventory.count(respond)):
                # runs the on_drop method
                items[respond].on_drop()
                # removes item from player's inventory
                player_1.inventory.remove(respond)
                # adds item to the room
                player_1.current_room.items.append(str(items[respond]))
            else:
                print(f'You do not have {respond} or {respond} is an invalid input')
        # if player types 'q', it will quit the game
        elif(respond == 'q'):
            print(f'I understand {name}, come back whenever you feel ready, goodbye.')
            game_on = False
        # if player types 'inventory', it will show info of inventory
        elif(respond == 'inventory'):
            print(f'Inventory there is {len(player_1.inventory)} amount of items in your inventory. {player_1.inventory}')
        #  provides the location of the player
        elif(respond == 'location'):
            print(f'Your location is {player_1.current_room.name}')
        #  provides the status of the player
        elif(respond == 'status'):
            print(f'Your current health is {player_1.health}, your current attack is {player_1.attack}')
        #  provides options for player to use
        elif(respond == 'help'):
            print('''
            You can move by typing 'n' to go north, 's' to go south, 'w' to go west and 'e' to go east.
            You can type 'search' to search the area for items
            You can type 'drop' to drop an item of your choice if you have it in your inventory.
            You can type 'inventory' to check what you currently have in your inventory.
            You can type 'location' if you want to confirm where you are.
            You can type 'status' to show what is your current health / attack.
            ''')
        # else:
        #     print('The value you typed is incorrect???????????')
    elif(text == 'no'):
        print(f'I understand {name}, come back whenever you feel ready, goodbye!')
        game_on = False
    else:
        print('The value you typed is incorrect, choose one of the following: "yes" / "no"')

