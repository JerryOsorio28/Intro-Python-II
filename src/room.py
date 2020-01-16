# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[], enemies=[]):
        self.name = name
        self.description = description
        self.items = []
        self.enemies = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __repr__(self):
        return f'{self.name}, {self.description}'
