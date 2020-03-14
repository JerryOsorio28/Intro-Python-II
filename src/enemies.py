class Enemies:
    def __init__(self, name, health=100, attack=20, dead=False):
        self.name = name
        self.health = health
        self.attack = attack
        self.dead = dead
    
    def on_attack(self):
        return self.attack

    def __repr__(self):
        return self.name
    