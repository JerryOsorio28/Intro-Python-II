# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, health=100, attack=10, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        self.health = health
        self.attack = attack
    
    def on_attack(self):
        return self.attack

    def __repr__(self):
        return self.name
