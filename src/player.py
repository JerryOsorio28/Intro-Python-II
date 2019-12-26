# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.inventory = []
        self.current_room = current_room 
    def __str__(self):
        return f"{self.name}'s location is {self.current_room}"
# player = Player('Jerry', 'outside')
# print(player)
