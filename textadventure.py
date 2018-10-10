"""
Text adventure
"""
import random

WATER_TYPES = ["creek","river","lake","stream","waterfall"]
GROUND_TYPES = ["grassy","rocky","sandy"]
ATTRIBUTE_TYPES = ["trees","cliffs"]
LEVEL_TYPES = ["mountains","lowlands","highlands"]

class Object():
    """ Object class. """

    def __init__(self):
        self.x = None
        self.y = None
        self.water = None
        self.ground = None
        self.attribute = None
        self.level = None

    def setup(self, x, y):
        self.x = x
        self.y = y

        water_chance = random.randint(1, 10)
        self.water = random.choice(GROUND_TYPES)
        self.ground = random.choice(ATTRIBUTE_TYPES)
        self.attribute = random.choice(LEVEL_TYPES)
        if water_chance >= 4:
            self.water = random.choice(WATER_TYPES)

class Player():
    """ Player class. """

    def __init__(self):
        self.x = None
        self.y = None

    def setup(self):
        self.x = 0
        self.y = 0

class World():
    """ Main application class. """

    def __init__(self):
        pass

    def setup(self):
        self.player = Player()
        self.player.setup()
        self.objects = []
        # TODO: fill world with objects

    def on_draw(self): 
        """ Render the screen. """

        # teken speler
        print("Player is: ", self.player.x, self.player.y)

        # teken objecten
        for object in self.objects:
            # teken object
            print("object op: ", object.x, object.y)
            print("De ground is: ", object.ground)


    def on_update(self):
        # TODO: alle geldigde instructies in een lijst zetten
        # TODO: user input checken (geen cijfers etc.)
        # TODO: user input naar lower case?
        instruction = input("What to do?")
        if instruction == "up":
            self.player.y += 1
        # TODO: other instructions


        # TODO: check if terrain is undiscovered
            # if so, generate
        new_object = Object()
        new_object.setup(self.player.x, self.player.y)
        self.objects.append(new_object)

def main():
    world = World()
    world.setup()
    while True:
        world.on_update()
        world.on_draw()


if __name__ == "__main__":
    main()