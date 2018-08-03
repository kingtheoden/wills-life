from random import choice


class Awareness:

    def __init__(self):
        self.immediate = []
        self.outer = []

    def inner_get(self, type_of_thing):
        list_of_things = []

        for tile in self.immediate:
            if type(tile) is type_of_thing or issubclass(type(tile), type_of_thing):
                list_of_things.append(tile)

        if len(list_of_things) > 0:
            return choice(list_of_things)
        else:
            return None

    def get_in_front(self, dir_x, dir_y):
        if dir_x == -1:
            thing = self.immediate[3]
        elif dir_y == -1:
            thing = self.immediate[2]
        elif dir_x == 1:
            thing = self.immediate[1]
        elif dir_y == 1:
            thing = self.immediate[0]
        else:
            thing = None
        return thing

    def get_nearest(self, type_of_thing):
        nearest_thing = None
        distance_of_thing = -1
        for tile in self.outer:
            if type(tile[0]) is type_of_thing and (nearest_thing is None or tile[1] < distance_of_thing):
                nearest_thing = tile[0]
                distance_of_thing = tile[1]
        return nearest_thing

    def count_in_awareness(self, type_of_thing):
        result = 0
        for thing in self.outer:
            if issubclass(type(thing[0]), type_of_thing):
                result += 1
        return result

