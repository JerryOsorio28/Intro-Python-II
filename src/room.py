# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return '{}, {}'.format(self.name, self.description)

# room = Room("Outside Cave Entrance", "North of you, the cave mount beckons")
# print(room)