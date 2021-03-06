from abc import ABCMeta

from emptyspace import EmptySpace
from life import Life


class DeadAnimal(Life, metaclass=ABCMeta):

    def __init__(self, x, y):
        self.death_counter = 0
        self.death_cap = 350

        Life.__init__(self, x, y)

    def move(self):
        pass

    def propagate(self):
        pass

    def die(self):
        if self.death_counter <= self.death_cap:
            self.death_counter += 1

        if self.death_counter >= self.death_cap:
            return EmptySpace(self.pos_x, self.pos_y)
        else:
            return None

    def get_vision(self):
        return 1

    def get_ticks_per_move(self):
        return 1
