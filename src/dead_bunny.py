from dead_animal import DeadAnimal


class DeadBunny(DeadAnimal):

    def __init__(self, x, y):
        DeadAnimal.__init__(self, x, y)

    def get_colour(self):
        return self.BURLYWOOD


