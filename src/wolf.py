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
        if self.sees_lots_of_prey:
            return 25 * self.get_ticks_per_move()
        else:
            return 150 * self.get_ticks_per_move()

    def get_eat_thresh(self):
        if self.sees_lots_of_prey:
            return 5 * self.get_ticks_per_move()
        else:
            return 40 * self.get_ticks_per_move()

    def __init__(self, x, y):
        Animal.__init__(self, x, y)

    def get_dead_animal(self):
        return DeadWolf(self.pos_x, self.pos_y)

    def get_death_age(self):
        return 1000 * self.get_ticks_per_move()

    def get_hunger_death(self):
        return 400 * self.get_ticks_per_move()

    def get_vision(self):
        return 10

    def get_ticks_per_move(self):
        if self.sees_prey:
            return 3
        else:
            return 6

    def get_colour(self):
        return self.BLUE

    def get_animal(self, x, y):
        return Wolf(x, y)

    def get_prey(self):
        return Bunny

    def get_meals_until_procreation(self):
        return 3
