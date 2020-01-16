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

