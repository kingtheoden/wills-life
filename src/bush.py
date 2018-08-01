from dead_bunny import DeadBunny
from dead_bush import DeadBush
from emptyspace import EmptySpace
from life import Life
from random import randint, choice


class Bush(Life):

    def __init__(self, x, y, land):
        self.sun = 0
        self.sun_cap = 100 + randint(0, 100)
        self.death_counter = 0
        self.death_cap = 200
        Life.__init__(self, x, y, land)

    def get_ticks_per_move(self):
        return 1

    def move(self):
        pass

    def propagate(self):
        """

        :return: Thing
        """

        empty_spots = []
        plant_counter = 0
        has_empty = False
        self.get_immediate_awareness(self.land)

        for tile in self.awareness.immediate:
            if type(tile) is EmptySpace:
                empty_spots.append(tile)
                has_empty = True
            elif type(tile) is Bush:
                plant_counter += 1

        if plant_counter >= 4:
            self.increase_death()
            self.decrease_sun()
        elif plant_counter == 3:
            pass
        else:
            self.decrease_death()
            self.increase_sun()

        dead_bush = self.awareness.inner_get(DeadBush)
        dead_bunny = self.awareness.inner_get(DeadBunny)

        if has_empty and plant_counter < 4 and (self.sun >= self.sun_cap or ((dead_bunny is not None or
                                                dead_bush is not None) and self.sun >= self.sun_cap / 2)):
            rand_empty_space = choice(empty_spots)
            self.sun = 0
            return Bush(rand_empty_space.pos_x, rand_empty_space.pos_y, self.land)
        else:
            return None

    def die(self):
        """

        :param:
        :return: boolean
        """
        if self.death_counter >= self.death_cap:
            return DeadBush(self.pos_x, self.pos_y, self.land)
        else:
            return None

    def get_colour(self):
        return self.LAWN_GREEN

    def get_vision(self):
        return 1

    def increase_sun(self):
        if self.sun <= self.sun_cap:
            self.sun += 1

    def decrease_sun(self):
        if self.sun > 0:
            self.sun -= 1

    def increase_death(self):
        if self.death_counter <= self.death_cap:
            self.death_counter += 1

    def decrease_death(self):
        if self.death_counter > 0:
            self.death_counter -= 1


