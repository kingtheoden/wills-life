from abc import ABCMeta, abstractmethod

from awareness import Awareness
from thing import Thing
from void import VoidSpace


class Life(Thing, metaclass=ABCMeta):

    def __init__(self, x, y):
        self.awareness = Awareness()
        self.land = None
        Thing.__init__(self, x, y)

    @abstractmethod
    def move(self): raise NotImplementedError

    @abstractmethod
    def propagate(self): raise NotImplementedError

    @abstractmethod
    def die(self): raise NotImplementedError

    @abstractmethod
    def get_vision(self):
        raise NotImplementedError

    @abstractmethod
    def get_ticks_per_move(self):
        raise NotImplementedError

    @staticmethod
    def increase(counter, limit):
        if counter < limit:
            return counter + 1
        return counter

    def get_awareness(self, land):
        self.get_immediate_awareness(land)
        if self.get_vision() > 1:
            self.get_outer_awareness(land)

    def get_immediate_awareness(self, land):
        immediate_awareness = []

        for x in range(4):
            check_x = self.pos_x + self.DIRECTIONS[x][0]
            check_y = self.pos_y + self.DIRECTIONS[x][1]
            if check_x >= land.size or check_x < 0 or check_y >= land.size or check_y < 0:
                immediate_awareness.append(VoidSpace(check_x, check_y))
            else:
                immediate_awareness.append(land.get(check_x, check_y))

        self.awareness.immediate = immediate_awareness

    def get_outer_awareness(self, land):
        outer_awareness = []

        for dy in range(self.get_vision()*2):
            y = self.pos_y + self.get_vision() - dy
            for dx in range(self.get_vision()*2):
                x = self.pos_x - self.get_vision() + dx

                if not (x == self.pos_x and y == self.pos_y):
                    if x >= land.size or x < 0 or y >= land.size or y < 0:
                        pass
                    else:
                        outer_awareness.append([land.get(x, y), abs(x - self.pos_x) + abs(y - self.pos_y)])

        self.awareness.outer = outer_awareness

    def find_dir(self, n1, n2):

        if n1 > n2:
            dir = -1
        elif n1 < n2:
            dir = 1
        else:
            dir = 0
        return dir






