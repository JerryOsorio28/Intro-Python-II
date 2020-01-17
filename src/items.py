class Items:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

    def on_take(self):
        print(f'You picked a {self.name}')

    def on_drop(self):
        print(f'You have dropped the {self.name}')
    
    def __repr__(self):
        return f'{self.name}'

class Potion(Items):
    def __init__(self, name, attack, health=30):
        self.health = health
        super().__init__(name, attack)
    
    def __repr__(self):
        return self.health
    


