from life import Life
from animal import Animal
from bush import Bush
from dead_bunny import DeadBunny
from dead_bush import DeadBush
from dead_wolf import DeadWolf
from emptyspace import EmptySpace


class Bunny(Animal):
    def sees_lots_of_prey_check(self, num_of_prey):
        return num_of_prey >= self.get_vision() * self.get_vision() / 2

    def can_trample(self, thing):
        return thing is EmptySpace or thing is DeadBunny or thing is DeadBush or thing is DeadWolf

    def get_hunger_thresh(self):
        return 50 * self.get_ticks_per_move()

    def get_eat_thresh(self):
        return 5 * self.get_ticks_per_move()

    def __init__(self, x, y):
        self.check_awareness_counter = 50
        self.check_awareness_threshold = 50
        Animal.__init__(self, x, y)

    def move(self):
        if self.sees_lots_of_prey:
            return Animal.move(self)
        else:
            self.check_awareness_counter = Life.increase(self.check_awareness_counter, self.check_awareness_threshold)
            if self.check_awareness_counter >= self.check_awareness_threshold:
                self.check_awareness_counter = 0
                self.get_awareness(self.land)
                num_of_prey = self.awareness.count_in_awareness(self.get_prey())
                self.sees_lots_of_prey = self.sees_lots_of_prey_check(num_of_prey)
            if self.can_move():
                return self.laze_about()

    def get_dead_animal(self):
        return DeadBunny(self.pos_x, self.pos_y)

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
        return Bunny(x, y)

    def get_prey(self):
        return Bush

    def get_meals_until_procreation(self):
        return 4
