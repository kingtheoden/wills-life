from abc import ABCMeta, abstractmethod


class Thing(metaclass=ABCMeta):
    # Define some colours
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GREY = (169, 169, 169)
    OLIVE_DRAB = (107, 142, 35)
    LAWN_GREEN = (124, 252, 0)
    CORNFLOWER_BLUE = (100, 149, 237)
    SIENNA = (160, 82, 45)
    BURLYWOOD = (222, 184, 135)

    DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # NESW

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    @abstractmethod
    def get_colour(self): raise NotImplementedError
