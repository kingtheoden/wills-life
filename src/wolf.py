from animal import Animal
from bunny import Bunny
from bush import Bush
from dead_bunny import DeadBunny
from dead_bush import DeadBush
from dead_wolf import DeadWolf
from emptyspace import EmptySpace


class Wolf(Animal):

    def can_trample(self, thing):
        return thing is EmptySpace or thing is Bush or thing is DeadBunny or thing is DeadBush or thing is DeadWolf

    def get_hunger_thresh(self):
        return 300 * self.get_ticks_per_move()

    def get_eat_thresh(self):
        return 25 * self.get_ticks_per_move()

    def __init__(self, x, y, land):
        Animal.__init__(self, x, y, land)

    def get_dead_animal(self):
        return DeadWolf(self.pos_x, self.pos_y, self.land)

    def get_death_age(self):
        return 2000 * self.get_ticks_per_move()

    def get_hunger_death(self):
        return 400 * self.get_ticks_per_move()

    def get_vision(self):
        return 6

    def get_ticks_per_move(self):
        if self.sees_prey:
            return 3
        else:
            return 6

    def get_colour(self):
        return self.BLUE

    def get_animal(self, x, y):
        return Wolf(x, y, self.land)

    def get_prey(self):
        return Bunny

    def get_meals_until_procreation(self):
        return 3
