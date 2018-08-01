from emptyspace import EmptySpace


class Land:

    def __init__(self, size):
        self.land_list = []
        self.spawn_empty_land(size)
        self.size = size

    def spawn_empty_land(self, size):

        for x in range(size):
            li = []
            for y in range(size):
                    li.append(EmptySpace(x, y))
            self.land_list.append(li)

    def put(self, thing, x, y):
        self.land_list[x][y] = thing

    def get(self, x, y):
        return self.land_list[x][y]

    def swap(self, thing_1, thing_2):
        old_pos_x = thing_1.pos_x
        old_pos_y = thing_1.pos_y

        self.put(thing_2, thing_1.pos_x, thing_1.pos_y)
        self.put(thing_1, thing_2.pos_x, thing_2.pos_y)

        thing_1.set_position(thing_2.pos_x, thing_2.pos_y)
        thing_2.set_position(old_pos_x, old_pos_y)

    def remove(self, thing):
        self.land_list[thing.pos_x][thing.pos_y] = EmptySpace(thing.pos_x, thing.pos_y)




