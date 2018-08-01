from emptyspace import EmptySpace
from life import Life


class DeadBush(Life):

    def __init__(self, x, y, land):
        self.death_counter = 0
        self.death_cap = 350
        self.alone = False

        Life.__init__(self, x, y, land)

    def get_ticks_per_move(self):
        return 1

    def move(self):
        pass

    def propagate(self):
        if self.death_counter <= self.death_cap:
            self.death_counter += 1
        return None

    def die(self):
        if self.death_counter >= self.death_cap:
            return EmptySpace(self.pos_x, self.pos_y)
        else:
            return None

    def get_colour(self):
        return self.OLIVE_DRAB

    def get_vision(self):
        return 1
