from emptyspace import EmptySpace
from life import Life


class DeadBunny(Life):

    def __init__(self, x, y, land):
        self.death_counter = 0
        self.death_cap = 350

        Life.__init__(self, x, y, land)

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

    def get_colour(self):
        return self.BURLYWOOD

    def move(self):
        pass
