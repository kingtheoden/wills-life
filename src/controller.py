from animal import Animal
from emptyspace import EmptySpace
from life import Life


class Controller:

    def __init__(self, land, drawer):
        self.land = land
        self.drawer = drawer
        self.bios = []

    def tick(self):
        for life in self.bios:
            move = life.move()
            if move is not None:

                if issubclass(type(life), Animal) and (type(move) is life.get_prey() or life.can_trample(type(move))):
                    self.remove(move)
                    new_move = EmptySpace(move.pos_x, move.pos_y)
                    move = new_move
                    self.put(move)

                self.swap(life, move)

            new_life = life.propagate()
            if new_life is not None:
                self.put(new_life)

            death = life.die()

            if death is not None:
                self.remove(life)
                self.put(death)

    def swap(self, thing1, thing2):
        self.land.swap(thing1, thing2)
        self.drawer.update([thing1, thing2])

    def put(self, thing):
        if issubclass(type(thing), Life):
            thing.land = self.land
        self.land.put(thing, thing.pos_x, thing.pos_y)

        if issubclass(type(thing), Life):
            self.bios.append(thing)

        self.drawer.update([thing])

    def remove(self, thing):
        self.land.remove(thing)
        if issubclass(type(thing), Life):
            self.bios.remove(thing)

    def print_info(self):
        for x in range(self.land.size):
            for y in range(self.land.size):
                print(type(self.land.land_list[x][y]), x, y, end=' ')
            print()

    def print_tmi(self):
        for x in range(self.land.size):
            for y in range(self.land.size):
                print(self.land.land_list[x][y], x, y, end=' ')
            print()


