class Items:
    def __init__(self, name):
        self.name = name

    def on_take(self):
        return f'You picked the {self.name}'
    
    def __repr__(self):
        return f'{self.name}'

