from animal import Animal
from bush import Bush
from dead_bunny import DeadBunny
from dead_bush import DeadBush
from dead_wolf import DeadWolf
from emptyspace import EmptySpace


class Bunny(Animal):
    def can_trample(self, thing):
        return thing is EmptySpace or thing is DeadBunny or thing is DeadBush or thing is DeadWolf

    def get_hunger_thresh(self):
        return 50 * self.get_ticks_per_move()

    def get_eat_thresh(self):
        return 5 * self.get_ticks_per_move()

    def __init__(self, x, y, land):
        Animal.__init__(self, x, y, land)

    def get_dead_animal(self):
        return DeadBunny(self.pos_x, self.pos_y, self.land)

    def get_death_age(self):
        return 500 * self.get_ticks_per_move()

    def get_hunger_death(self):
        return 80 * self.get_ticks_per_move()

    def get_vision(self):
        return 5

    def get_ticks_per_move(self):
        return 5

    def get_colour(self):
        return self.SIENNA

    def get_animal(self, x, y):
        return Bunny(x, y, self.land)

    def get_prey(self):
        return Bush

    def get_meals_until_procreation(self):
        return 4
