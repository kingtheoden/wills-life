from abc import ABCMeta, abstractmethod
from random import choice, randint

from emptyspace import EmptySpace
from life import Life


class Animal(Life, metaclass=ABCMeta):
    def __init__(self, x, y):

        self.sees_prey = False  # Must come before self.get() methods to properly define thresholds

        self.age = 0
        self.hunger = 0
        self.ready_to_breed = False
        self.is_hungry = False
        self.could_eat = False
        self.meals_since_procreation = 0
        self.death_age = self.get_death_age()
        self.hunger_death = self.get_hunger_death()
        self.hunger_thresh = self.get_hunger_thresh()
        self.eat_thresh = self.get_eat_thresh()
        self.move_counter = randint(0, self.get_ticks_per_move() - 1)

        Life.__init__(self, x, y)

    @abstractmethod
    def get_dead_animal(self):
        raise NotImplementedError

    @abstractmethod
    def get_death_age(self):
        raise NotImplementedError

    @abstractmethod
    def get_hunger_death(self):
        raise NotImplementedError

    @abstractmethod
    def get_hunger_thresh(self):
        raise NotImplementedError

    @abstractmethod
    def get_eat_thresh(self):
        raise NotImplementedError

    @abstractmethod
    def get_meals_until_procreation(self):
        raise NotImplementedError

    @abstractmethod
    def get_animal(self, x, y):
        raise NotImplementedError

    @abstractmethod
    def get_prey(self):
        raise NotImplementedError

    @abstractmethod
    def can_trample(self, thing):
        raise NotImplementedError

    def eat(self):
        self.meals_since_procreation = Life.increase(self.meals_since_procreation, self.get_meals_until_procreation())
        self.hunger = 0
        self.is_hungry = False
        self.could_eat = False
        if self.meals_since_procreation >= self.get_meals_until_procreation():
            self.ready_to_breed = True

    def die(self):
        self.age = Life.increase(self.age, self.death_age)
        self.hunger = Life.increase(self.hunger, self.hunger_death)

        if self.hunger > self.eat_thresh:
            self.could_eat = True

        if self.hunger > self.hunger_thresh:
            self.is_hungry = True

        if self.age >= self.death_age:
            return self.get_dead_animal()
        elif self.hunger >= self.hunger_death:
            return self.get_dead_animal()
        else:
            return None

    def propagate(self):
        self.get_immediate_awareness(self.land)
        if self.ready_to_breed:
            other_animal = self.awareness.inner_get(type(self))
            if other_animal is not None and other_animal.ready_to_breed:
                empty = self.awareness.inner_get(EmptySpace)
                if empty is not None:
                    self.meals_since_procreation = 0
                    self.ready_to_breed = False
                    other_animal.meals_since_procreation = 0
                    other_animal.ready_to_breed = False
                    return self.get_animal(empty.pos_x, empty.pos_y)

    def move(self):
        if not self.can_move():
            return None

        self.get_awareness(self.land)

        self.sees_prey = False

        if self.is_hungry:
            move = self.hungry_move()
        elif self.ready_to_breed:
            move = self.move_toward_thing(type(self))
        elif self.could_eat:
            move = self.hungry_move()
        else:
            move = self.laze_about()

        return move

    def hungry_move(self):
        nearest_thing = self.awareness.get_nearest(self.get_prey())
        self.sees_prey = type(nearest_thing) is self.get_prey()

        move = self.move_toward_thing(self.get_prey())
        if type(move) is self.get_prey():
            self.eat()
        elif type(move) is type(self):
            move = self.laze_about()
        return move

    def can_move(self):
        if self.move_counter >= self.get_ticks_per_move():
            self.move_counter = 0
            return True
        else:
            self.move_counter += 1
            return False

    def move_toward(self, thing):
        dir_x = self.find_dir(self.pos_x, thing.pos_x)
        dir_y = self.find_dir(self.pos_y, thing.pos_y)

        thing_x = self.awareness.get_in_front(dir_x, 0)
        thing_y = self.awareness.get_in_front(0, dir_y)

        thing_opposite_x = self.awareness.get_in_front(-dir_x, 0)
        thing_opposite_y = self.awareness.get_in_front(0, -dir_y)

        if self.can_trample(type(thing_x)) and self.can_trample(type(thing_y)):
            li = [thing_x, thing_y]
            return choice(li)
        elif self.can_trample(type(thing_x)):
            return thing_x
        elif self.can_trample(type(thing_y)):
            return thing_y
        elif dir_x is not 0 and self.can_trample(type(thing_opposite_x)):
            return thing_opposite_x
        elif dir_y is not 0 and self.can_trample(type(thing_opposite_y)):
            return thing_opposite_y
        else:
            return None

    def move_toward_thing(self, type_of_thing):
        immediate_thing = self.awareness.inner_get(type_of_thing)
        if immediate_thing is not None:
            return immediate_thing
        nearest_thing = self.awareness.get_nearest(type_of_thing)
        if nearest_thing is not None:
            return self.move_toward(nearest_thing)
        return self.laze_about()

    def laze_about(self):
        return None
        empty = self.awareness.inner_get(EmptySpace)
        return empty

